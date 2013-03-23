import sys
import StringIO
import contextlib

from celery.decorators import task

from .models import Job

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

@task()
def run_job(job):
    if job.status == 'submitted':
        job.status = 'running'
        job.save()
        try:
            with stdoutIO() as s:
                exec(job.code)
            job.status = 'completed'
            job.output = 'Success: %s' % s.getvalue()
        except Exception as ex:
            job.status = 'error'
            job.output = 'Error: %s' % ex[0]
        job.save()
