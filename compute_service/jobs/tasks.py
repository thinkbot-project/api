import os
import StringIO

from celery.decorators import task

from .helpers import RedirectStdStreams, make_sure_path_exists
from .models import Job

def augment_job_for_output(job):
    current_path = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(current_path, "..", "results", str(job.pk))
    make_sure_path_exists(output_path)
    for variable in job.variables.all():
        if variable.format == "vtk":
            output_code = """
{0}_file = File("{1}/{0}.pvd")
{0}_file << {0}
""".format (variable.name, output_path)
    return output_code

@task()
def run_job(job):
    if job.status == 'submitted':
        job.status = 'running'
        job.stdout = ''
        job.stderr = ''
        job.exception = ''
        augment_job_for_output(job)
        job.save()
        try:
            local_stdout = StringIO.StringIO()
            local_stderr = StringIO.StringIO()
            with RedirectStdStreams(stdout=local_stdout, stderr=local_stderr):
                output_code = augment_job_for_output(job)
                exec(job.code + output_code)
            job.status = 'completed'
            job.stdout = local_stdout.getvalue()

        except Exception as ex:
            job.status = 'error'
            job.stderr = local_stderr.getvalue()
            job.exception = ex[0]
        job.save()
