from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test-get", TestGetApi.as_view(), name = "test-get-api"),
    path("test-post", TestPostApi.as_view(), name = "test-post-api"),
]
