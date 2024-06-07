from django.contrib import admin
from .models import Campaign, Subscriber


class CampaignModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'craeted_at', 'updated_at')
    search_fields = ('title',)





admin.site.register(Campaign, CampaignModelAdmin)
admin.site.register(Subscriber)
