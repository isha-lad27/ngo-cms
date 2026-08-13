from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: HttpResponse("NGO CMS is running!")),
    path("api/about-us/", include("aboutus.urls")),
    path("api/", include("home.urls")),
]
