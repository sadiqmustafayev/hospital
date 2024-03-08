from django.urls import path
from .views import ContactViewSet, ContactDetailViewSet, SubscriberAPIview
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

urlpatterns = [
  path('Contact/', ContactViewSet.as_view()),
  path('subscriber/', SubscriberAPIview.as_view(), name='subscriber'),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
