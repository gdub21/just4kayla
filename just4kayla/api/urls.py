from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoute, name = "routes"),
]