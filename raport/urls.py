from .views import rapor_detay, rapor_search, rapor_add
from django.urls import path
from django.conf.urls import handler403
from . import views
from django.urls import path

urlpatterns = [
  path('rapor/<int:rapor_id>/', rapor_detay, name='rapor_detay'),
  path('search/', rapor_search, name='rapor_search'),
  path('add/', rapor_add, name='rapor_add'),
  path('list/', views.rapor_list, name='rapor_list'),
]
