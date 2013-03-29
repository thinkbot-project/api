from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Job

class JobTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')

    def test_model_creation(self):
        job = Job.objects.create(
            environment = 'python27',
            code = """
print "Hello, World!"
foo = 1
bar = 2
print "1 + 2 = ", foo + bar
""",
            owner = self.user,
            status = 'submitted')
        self.assertTrue(isinstance(job, Job))
