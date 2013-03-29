from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Job

class JobSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    results = serializers.RelatedField(many=True)

    class Meta:
        model = Job
        fields = ('url', 'status', 'owner', 'created', 'modified',
                  'name', 'environment', 'code', 'variables', 'results',
                  'stdout', 'stderr', 'exception')
        read_only_fields = ('status', 'stdout', 'stderr', 'exception',
                            'max_runtime')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'jobs')
