from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from users.views import Register

app_name = "user"

urlpatterns = [
    path(
        "register",
        TemplateView.as_view(template_name="users/register.html"),
        name="register",
    ),
]
