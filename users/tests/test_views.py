from django.test import TestCase, Client
from django.urls import reverse
from users import views
from users import models
from django.contrib.auth.models import User

import secrets


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.username = secrets.token_hex(4)
        self.email = f'{self.username}@mail.com'
        self.password = secrets.token_hex(4)

