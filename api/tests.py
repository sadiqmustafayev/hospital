from django.test import TestCase
from django.contrib.auth import get_user_model


class BaseUserTestCase(TestCase):

  def test_create_user(self):
    User = get_user_model()
    user = User.objects.create_user(username='testuser',
                                    email='testuser@example.com',
                                    password='testpassword')
    self.assertEqual(user.username, 'testuser')
    self.assertEqual(user.email, 'testuser@example.com')
    self.assertTrue(user.check_password('testpassword'))
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)

  def test_create_superuser(self):
    User = get_user_model()
    superuser = User.objects.create_superuser(username='admin',
                                              email='admin@example.com',
                                              password='adminpassword')
    self.assertEqual(superuser.username, 'admin')
    self.assertEqual(superuser.email, 'admin@example.com')
    self.assertTrue(superuser.check_password('adminpassword'))
    self.assertTrue(superuser.is_staff)
    self.assertTrue(superuser.is_superuser)
