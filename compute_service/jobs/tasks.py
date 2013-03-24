import StringIO

from celery.decorators import task

from .helpers import RedirectStdStreams
from .models import Job

@task()
def run_job(job):
    if job.status == 'submitted':
        job.status = 'running'
        job.output = ''
        job.save()
        try:
            local_stdout = StringIO.StringIO()
            local_stderr = StringIO.StringIO()
            with RedirectStdStreams(stdout=local_stdout, stderr=local_stderr):
                exec(job.code)
            job.status = 'completed'
            job.output += 'stdout: "%s"' % local_stdout.getvalue()
        except Exception as ex:
            job.status = 'error'
            job.output += ', stderr: "%s"' % local_stderr.getvalue()
            job.output += ', exception: "%s"' % ex[0]

        job.save()
