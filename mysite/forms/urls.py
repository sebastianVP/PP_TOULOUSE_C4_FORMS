from django.contrib import admin
from django.urls import path
from . import views

app_name = 'forms'

urlpatterns=[
    path("",views.index,name='mi_form')
]

"""
Queremos tener:

http://127.0.0.1:8000/
En lugar de:

http://127.0.0.1:8000/path_de_url
"""