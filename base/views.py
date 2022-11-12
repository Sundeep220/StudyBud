from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request, id):
    room = Room.objects.get(id=id)
    messages = room.message_set.all()
    context = {'room': room, 'messages': messages}
    return render(request, 'base/room.html', context)
