from django.contrib.auth.models import User

from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Job
from .serializers import JobSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'jobs': reverse('job-list', request=request, format=format)
    })

class JobResult(generics.SingleObjectAPIView):
    model = Job
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        job = self.get_object()
        exec(job.code)
        return Response(job)

class JobList(generics.ListCreateAPIView):
    model = Job
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Job
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
