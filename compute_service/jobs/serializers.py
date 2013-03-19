from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from jobs.models import Job

class JobSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
#    highlight = serializers.HyperlinkedIdentityField(view_name='job-highlight', format='html')

    class Meta:
        model = Job
        fields = ('url', 'owner',
                  'name', 'environment', 'version', 'code', 'output', 'max_runtime')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'jobs')
