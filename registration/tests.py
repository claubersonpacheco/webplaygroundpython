from os.path import exists

from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        User.objects.create(username='testuser', email='teste@test.com', password='test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='testuser').exists()
        self.assertEqual(exists, True)