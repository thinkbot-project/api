from celery.decorators import task

from .models import Job

@task()
def run_job(job):
    if job.status == 'submitted':
        job.status='running'
        try:
            exec(job.code)
            job.status = 'completed'
        except RuntimeError as ex:
            job.status = 'error'
            job.output = "Exception: %s" % ex[0]
        job.save()
