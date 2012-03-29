from django.shortcuts import render_to_response 

from music.concerts.models import Event


def home(request):
    greeting = "Welcome To My Backstage Pass"
    event = Event.objects.all()
    return render_to_response('home.html', {
        'event': event, 
        'greeting': greeting, 
    })

def detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render_to_response('detail.html', {
        'event': event,
    })
