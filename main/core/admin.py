from django.contrib import admin
from .models import Destination, Newsletter, ShareStory

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
	list_display = ('dest_slider_title', 'dest_location', 'dest_content', 'created')
	list_filter = ('dest_location',)
	search_fields = ('dest_profile_title', 'dest_content')

admin.site.register(Newsletter)
admin.site.register(ShareStory)