"""KNN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from core.urls import urlpatterns as core_urls
from baseuser.urls import urlpatterns as baseuser_urlpatterns
from api.urls import urlpatterns as api_urlpatterns
from raport.urls import urlpatterns as raport_urlpatterns

urlpatterns = [
    path('api/', include((api_urlpatterns))),
    path('', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
  path('admin/', admin.site.urls),
  path('user/', include(baseuser_urlpatterns)),
  path('report/', include(raport_urlpatterns)),
  path('', include(core_urls)),
  path('i18n/', include('django.conf.urls.i18n')),
)

if 'rosetta' in settings.INSTALLED_APPS:
  urlpatterns += [re_path('translate/', include('rosetta.urls')) ]

