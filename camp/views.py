from django.shortcuts import render
from rest_framework import generics , response
from .models import Campaign, Subscriber
from .serializers import SubscriberSerializer, CampaignSerializer
from django.shortcuts import get_object_or_404


class CampaignListAPIView(generics.ListAPIView):
    
    serializer_class = CampaignSerializer


    def get_queryset(self):
        return Campaign.objects.all()
    
class CampaignDetailAPIView(generics.GenericAPIView):
    serializer_class = CampaignSerializer
    
    def get(self,request,slug):

        query_set = Campaign.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not Found')
    
class SubscribeToCampaignAPIView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        return Subscriber.objects.all()
    
class CampaignDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    serializer_class = CampaignSerializer

    queryset = Campaign.objects.all()

    lookup_field = 'slug'

class CampaignCreateAPIView(generics.CreateAPIView):
    serializer_class = CampaignSerializer



class CampaignSubscriberListAPIView(generics.ListAPIView):
    serializer_class = SubscriberSerializer

    
    def get_queryset(self):
        
        campaign_slug = self.kwargs['slug']

        campaign = get_object_or_404(Campaign, slug=campaign_slug)

        return Subscriber.objects.filter(campaign = campaign)


