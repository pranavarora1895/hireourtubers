from django.urls import path
from . import views

urlpatterns = [
    path('allinfo', views.allinfo, name="allinfo"),

]