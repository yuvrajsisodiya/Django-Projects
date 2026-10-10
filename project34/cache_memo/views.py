from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from .models import Channel
import time
# Create your views here.
def channel_list(request):
    channels = cache.get('channels')
    if not channels:
        channels = Channel.objects.all()
        cache.set('channels', channels, timeout=300)  # Cache for 5 minutes
        print("Cache miss: Fetching channels from database.")
    else:
        print("Cache hit: Fetching channels from cache.")
    return render(request, 'youtube/channel_list.html', {'channels': channels})

