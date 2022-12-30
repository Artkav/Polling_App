from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.polling_list, name='poll_list'),
    path('poll/<str:slug>', views.detail_view, name="poll"),
]

