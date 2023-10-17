from django.urls import path, include
from .views import *

app_name = "usuarios"

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("registro/", RegistroUsuarioView.as_view(), name="registro"),
]
