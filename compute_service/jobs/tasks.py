import os
import StringIO

from django.conf import settings

from celery.decorators import task

from .helpers import RedirectStdStreams
from .helpers import make_sure_path_exists, reset_job_output, job_output_path, job_output_code
from .models import Job, Result

@task()
def run_job(job):
    if job.status == 'submitted':
        reset_job_output(job)
        output_path = job_output_path(job)
        make_sure_path_exists(output_path)
        try:
            local_stdout = StringIO.StringIO()
            local_stderr = StringIO.StringIO()
            with RedirectStdStreams(stdout=local_stdout, stderr=local_stderr):
                output_code = job_output_code(job)
                exec(job.code + output_code) in globals()
            job.status = 'completed'
            job.stdout = local_stdout.getvalue()
            variables = job.variables.split(", ")
            for variable in variables:
                name, format = variable.split(".")
                if format == "vtk":
                    Result.objects.create(name=name,
                                          location=settings.BASE_URL + "/results/" + str(job.pk) + "/" + name + ".vtk",
                                          job=job)

        except Exception as ex:
            job.status = 'error'
            job.stderr = local_stderr.getvalue()
            job.exception = ex[0]
        job.save()
