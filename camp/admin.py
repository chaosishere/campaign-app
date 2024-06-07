from django.contrib import admin
from .models import Campaign, Subscriber


class CampaignModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'craeted_at', 'updated_at')
    search_fields = ('title',)
    list_per_page = 10


class SubscriberModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'campaign','craeted_at','updated_at')
    search_fields = ('email','campaign__title',)
    list_per_page = 10



admin.site.register(Campaign, CampaignModelAdmin)
admin.site.register(Subscriber, SubscriberModelAdmin)
