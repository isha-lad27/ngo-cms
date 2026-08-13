from django.urls import path
from .views import AboutUsAPIView


urlpatterns = [
    path('', AboutUsAPIView.as_view(), name='about-us-api'),
]