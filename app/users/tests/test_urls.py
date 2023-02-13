from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users import views


class TestUrls(SimpleTestCase):

    def test_profile_url_runs_correct_view(self):
        url = '/profile/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.update_user_and_profile)

    def test_profile_url_name_runs_correct_view(self):
        url = reverse('users:profile')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.update_user_and_profile)

    def test_register_url_runs_correct_view(self):
        url = '/register/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.register)

    def test_register_url_name_runs_correct_view(self):
        url = reverse('users:register')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.register)
