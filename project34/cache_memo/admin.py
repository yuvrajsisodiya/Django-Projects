from django.contrib import admin
from .models import Channel
# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'subscribers')
    search_fields = ('name', 'description')

