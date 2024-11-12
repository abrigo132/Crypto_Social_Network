from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from posts.views import CreatePost

urlpatterns = [
    path("api/v1/create/", CreatePost.as_view()),
]
