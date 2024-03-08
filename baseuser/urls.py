from django.urls import path
from django.contrib.auth import views as auth_views
from baseuser.views import register, CustomLoginView, login_view, delete_account
from . import views
from django.conf.urls import handler403
from django.conf import settings
# from django.contrib.auth.views import logout

urlpatterns = [
  path('login/', login_view, name='login'),
  path('register/', register, name='register'),
  path('edit/', views.profile_edit, name='profile_edit'),
  path('logout/',
       auth_views.LogoutView.as_view(next_page='home'),
       name='logout'),
  path('delete_account/', delete_account, name='delete_account'),
]
