from django.test import TestCase, Client
from django.urls import reverse


class TestUrls(TestCase):

  def setUp(self):
    self.client = Client()

  def test_rapor_search(self):
    response = self.client.get('/en/report/search/')
    self.assertEqual(response.status_code, 200)

  def test_user_login(self):
    response = self.client.get('/en/user/login/')
    self.assertEqual(response.status_code, 200)

  def test_user_register(self):
    response = self.client.get('/en/user/register/')
    self.assertEqual(response.status_code, 200)

  def test_home_url(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)

  def test_about_url(self):
    response = self.client.get(reverse('about'))
    self.assertEqual(response.status_code, 200)

  def test_appointment_url(self):
    response = self.client.get(reverse('appointment'))
    self.assertEqual(response.status_code, 200)

  def test_blogs_url(self):
    response = self.client.get(reverse('blog'))
    self.assertEqual(response.status_code, 200)

  def test_booking_list_url(self):
    response = self.client.get(reverse('booking_list'))
    self.assertEqual(response.status_code, 200)

  def test_contact_url(self):
    response = self.client.get(reverse('contact'))
    self.assertEqual(response.status_code, 200)

  def test_doctor_url(self):
    response = self.client.get(reverse('doctor'))
    self.assertEqual(response.status_code, 200)

  def test_error_url(self):
    response = self.client.get(reverse('error'))
    self.assertEqual(response.status_code, 200)

  def test_faq_url(self):
    response = self.client.get(reverse('faq'))
    self.assertEqual(response.status_code, 200)

  def test_service_details_url(self):
    response = self.client.get(reverse('service_details'))
    self.assertEqual(response.status_code, 200)

  def test_service_url(self):
    response = self.client.get(reverse('service'))
    self.assertEqual(response.status_code, 200)

  def test_services_url(self):
    response = self.client.get(reverse('services'))
    self.assertEqual(response.status_code, 200)


from django.test import TestCase
from core.forms import ContactForm


class TestContactForm(TestCase):

  def test_valid_form(self):
    form_data = {
      'name': 'John Doe',
      'email': 'johndoe@example.com',
      'phone_number': '1234567890',
      'message': 'This is a test message'
    }
    form = ContactForm(data=form_data)
    self.assertTrue(form.is_valid())

  def test_invalid_form(self):
    form_data = {
      'name': '',
      'email': 'johndoe@example.com',
      'phone_number': '1234567890',
      'message': ''
    }
    form = ContactForm(data=form_data)
    self.assertFalse(form.is_valid())
