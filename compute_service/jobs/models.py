from django.db import models

ENVIRONMENTS = [('fenics', 'The FEniCS Project')]
VERSIONS = [('1.1', '1.1')]

class Job(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='jobs')

    name = models.CharField(max_length=100, blank=True, default='')
    environment = models.CharField(max_length=100, choices=ENVIRONMENTS, default='fenics')
    version = models.CharField(max_length=20, choices=VERSIONS, default='1.1')
    code = models.TextField()
    output = models.CharField(max_length=50, default='u')
    max_runtime = models.IntegerField(default=60)

    class Meta:
        ordering = ('created',)
