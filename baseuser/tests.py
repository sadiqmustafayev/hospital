from django.test import TestCase, Client
from django.urls import reverse
from baseuser.models import BaseUser
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from baseuser.forms import BaseUserForm


###register TEST
class BaseUserRegistrationTest(TestCase):

  def setUp(self):
    self.register_url = reverse('register')
    self.login_url = reverse('login')
    self.user_data = {
      'username': 'testuser1111',
      'email': 'testuser@test.com',
      'first_name': 'Test',
      'last_name': 'User',
      'password1': 'Testpassword123',
      'password2': 'Testpassword123',
    }

  def test_register_view(self):
    response = self.client.get(self.register_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'register.html')
    self.assertContains(response, 'Register')

  def test_register_form(self):
    form = BaseUserForm(data=self.user_data)
    self.assertTrue(form.is_valid())

  def test_register_post_success(self):
    response = self.client.post(self.register_url, data=self.user_data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/en/', target_status_code=200)
    self.assertEqual(get_user_model().objects.count(), 1)

  def test_register_post_failure(self):
    # Test when passwords don't match
    self.user_data['password2'] = 'wrongpassword'
    response = self.client.post(self.register_url, data=self.user_data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'The two password fields did not match.')
    self.assertEqual(get_user_model().objects.count(), 0)


####LOGIN UCUN
class LoginTest(TestCase):

  def setUp(self):
    self.client = Client()
    self.login_url = reverse('login')
    self.user = BaseUser.objects.create_user(
      username='testuser1111',
      password='Testuser1111',
    )

  def test_login_view_success(self):
    response = self.client.post(self.login_url, {
      'username': 'testuser1111',
      'password': 'Testuser1111'
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/en/')

  def test_login_view_failure(self):
    response = self.client.post(self.login_url, {
      'username': 'testuser1111',
      'password': 'wrongpassword'
    })
    self.assertEqual(response.status_code, 200)
    self.assertContains(response,
                        "Please enter a correct username and password.")
