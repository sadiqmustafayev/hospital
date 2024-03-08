from core.models import Setting
from django.shortcuts import render
from baseuser.models import BaseUser
from core.models import Doctors, Contact ,Subscriber
from raport.models import AnalizRaport


def settings(request):
  return {'setting': Setting.objects.all()}

def report_count(request):
  return {'report_count': AnalizRaport.objects.count()}

def doctor_count(request):
  return {
    'doctor_count': Doctors.objects.count(),
  }

def user_count(request):
  return {
    'user_count': BaseUser.objects.count(),
  }

def contact_count(request):
  return {
    'contact_count': Contact.objects.count(),
  }

def subscriber_count(request):
  return {
    'subscriber_count': Subscriber.objects.count(),
  }