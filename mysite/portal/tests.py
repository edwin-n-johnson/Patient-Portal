from django.test import TestCase
from .models import Patient

# Create your tests here.
class PatientTestCase(TestCase):
    def setUp(self):
        print "PatientTestCase::setUp()"

    def test_placeholder(self):
        print "PatientTestCase::test_placeholder()"
        self.assertTrue(True)
