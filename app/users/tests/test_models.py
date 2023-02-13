from django.test import TestCase

from users.models import Profile
from django.contrib.auth.models import User

import secrets


class ProfileModelTestCase(TestCase):

    def setUp(self):
        username = secrets.token_hex(4)
        email = f'{username}@mail.com'
        password = secrets.token_hex(4)
        self.new_user = User.objects.create_user(username=username, email=email, password=password)
        self.new_profile = Profile.objects.get(user=self.new_user)

    def test_if_profile_creates_automatically(self):
        self.assertIsInstance(self.new_profile, Profile)

    def test_if_profiles_str_is_correct(self):
        self.assertEqual(str(self.new_profile), f"{self.new_user.username}'s profile")
