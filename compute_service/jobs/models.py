from django.db import models

from model_utils import Choices
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField


class Job(TimeStampedModel):
    STATUS = Choices('submitted', 'running', 'completed', 'failed')
    ENVIRONMENTS = Choices(('python27', 'Python (2.7)'),
                           ('fenics11', 'The FEniCS Project (1.1)'),
                           ('octave26', 'GNU Octave(2.6)'),
                           ('r215', 'R (2.15)'))

    name = models.CharField(max_length=100, blank=True, default='')
    environment = models.CharField(max_length=100, choices=ENVIRONMENTS, default='python27')
    code = models.TextField()
    output = models.CharField(max_length=50, default='stdout')
    max_runtime = models.IntegerField(default=60)

    owner = models.ForeignKey('auth.User', related_name='jobs')
    status = StatusField()

    class Meta:
        ordering = ('created',)
