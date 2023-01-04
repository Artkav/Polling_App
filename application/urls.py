from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PollingList.as_view(), name='poll_list'),
    path('poll/<str:slug>/', views.detail_view, name="poll"),
    # path('poll/<str:slug>/', views.PollingDetailView1.as_view(), name="poll"),
    path('create/', views.PollingCreateView.as_view(), name='create-poll'),
    path('vote/', views.create_vote, name='vote')
]

