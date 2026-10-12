from django.shortcuts import render
from django.core.cache import cache
from .models import Channel
# file based memoery
# Create your views here.
def channel_list_file(request):
    channels = cache.get('channels')
    if not channels:
        channels = Channel.objects.all()
        cache.set('channels', channels, timeout=65)  # Cache for 5 minutes
        print("DATA FETCHED FROM DATABASE")
    else:
        print("DATA FETCHED FROM CACHE")
    return render(request, 'channel_list_file.html', {'channels': channels})