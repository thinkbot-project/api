from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Job

class JobSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Job
        fields = ('url', 'status', 'owner', 'created', 'modified',
                 'name', 'environment', 'code', 'output', 'max_runtime')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'jobs')
