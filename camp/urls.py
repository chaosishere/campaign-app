from django.urls import path
from .views import CampaignListAPIView, CampaignDetailAPIView, SubscribeToCampaignAPIView, CampaignDetailUpdateAPIView, CampaignCreateAPIView, CampaignSubscriberListAPIView


urlpatterns = [
    path('campaigns/', CampaignListAPIView.as_view(), name='campaigns'),
    path('campaigns/create/', CampaignCreateAPIView.as_view(),name='create'),
    path('campaigns/<str:slug>/', CampaignDetailAPIView.as_view()),
    path('subscribe/', SubscribeToCampaignAPIView.as_view(), name='subscribe'),
    path('campaigns/update/<slug:slug>/', CampaignDetailUpdateAPIView.as_view()),
    path('campaigns/<slug:slug>/subscribers/', CampaignSubscriberListAPIView.as_view()),
]
