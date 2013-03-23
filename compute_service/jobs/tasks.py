from celery.decorators import task

from .models import Job

@task()
def run_job(job):
    if job.status == 'submitted':
        job.status = 'running'
        try:
            exec(job.code)
            job.status = 'completed'
        except Exception as ex:
            job.status = 'error'
            job.output = "Error: %s" % ex[0]
        job.save()
