from django.db import models
from django.contrib.auth.models import User

from model_utils import Choices
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from rest_framework.authtoken.models import Token


class Job(TimeStampedModel):
    STATUS = Choices('submitted', 'running', 'completed', 'failed')
    ENVIRONMENTS = Choices(('python27', 'Python (2.7)'),
                           ('fenics11', 'The FEniCS Project (1.1)'),
                           ('octave26', 'GNU Octave(2.6)'),
                           ('r215', 'R (2.15)'))

    name = models.CharField(max_length=100, blank=True, default='')
    environment = models.CharField(max_length=100, choices=ENVIRONMENTS, default='python27')
    code = models.TextField()
    variables = models.CharField(max_length=100, blank=True, default='')

    stdout = models.TextField(blank=True, default='')
    stderr = models.TextField(blank=True, default='')
    exception = models.TextField(blank=True, default='')

    max_runtime = models.IntegerField(default=60)

    owner = models.ForeignKey(User, related_name='jobs')
    status = StatusField()

    class Meta:
        ordering = ('created',)


class Result(models.Model):
    name = models.CharField(max_length=100)
    location = models.URLField()
    job = models.ForeignKey(Job, related_name='results')

    def __unicode__(self):
        return "%s" % self.location

# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


# FORMATS = Choices(('vtk', 'VTK'),
#                   ('json', 'JSON'),
#                   ('png', 'PNG'),
#                   ('svg', 'SVG'),
#                   ('xml', 'XML'),
#                   ('numpy', 'NumPy'))
