from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Job

class JobTests(TestCase):

    def setUp(TestCase):
        self.user = User.objects.create(username='test')

    def test_model_creation(self):
        job = Job.Object.create(
            environment = 'python27',
            code = """
print "Hello, World!"
foo = 1
bar = 2
print "1 + 2 = ", foo + bar
""",
            max_runtime = 60,
            owner = self.user,
            status = 'submitted')
        self.assertTrue(isinstance(job, Job))
