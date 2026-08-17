from django.urls import path
from . import views

urlpatterns = [
    path("", views.media_gallery, name="media_gallery"),
    path("api/", views.media_api, name="media_api"),
]