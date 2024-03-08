from core.views import base
from core import views, tasks
from django.urls import path
from django.conf.urls import handler403
from . import views

from core.views import base
from core.views import (
  home,
  about,
  appointment,
  booking_list,
  contact,
  doctor_details,
  error,
  faq,
  index_2,
  service_details,
  service,
  services,
  add_comment,
  blog_details,
  
  BlogsListView,
  DoctorsListView,
)
from django.urls import path

handler404 = 'myapp.views.my_custom_permission_denied_view'

urlpatterns = [
  path('', home, name='home'),
  path('about/', about, name='about'),
  path('appointment/', appointment, name='appointment'),
  path('blogs/', BlogsListView.as_view(), name='blog'),
  path('blogs/<slug:slug>/', blog_details, name='blog_details'),
  path('booking_list/', booking_list, name='booking_list'),
  path('contact/', contact, name='contact'),
  path('doctor/', DoctorsListView.as_view(), name='doctor'),
  path('doctor/<slug:slug>/', doctor_details, name='doctor_details'),
  path('error/', error, name='error'),
  path('search/', views.site_search, name='site_search'),
  path('doctors/search/', views.search_doctors, name='search_doctors'),
  path('faq/', faq, name='faq'),
  path('index-2/', index_2, name='index_2'),
  path('service-details/', service_details, name='service_details'),
  path('service/', service, name='service'),
  path('services/', services, name='services'),
  path('send_email/', views.send_email, name='send_email'),
  path('thank-you/', views.thank_you, name='thank-you'),
  path('blog/<slug:slug>/comment/', add_comment, name='add_comment'),
]
