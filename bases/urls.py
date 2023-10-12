from django.urls import path
from .views import *

#nombrar la aplicacion, y rutas mas clasificadas
app_name="core"

urlpatterns = [
    path('', primera_vista, name='primera_vista')
]