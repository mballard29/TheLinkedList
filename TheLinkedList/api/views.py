from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random
import datetime
from .models import User, Event
from .forms import UserForm, EventForm, UserSearchForm, EventSearchForm, JoinSearchForm, AggregateSearchForm
from django.template import RequestContext


# User functions

def user_list(request):
    users = User.objects.all()
    events = Event.objects.all()
    return render(request, 'api/user_list.html', {'users': users, 'events': events})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'api/user_detail.html', {'user': user})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'api/user_edit.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'api/user_edit.html', {'form': form})


def user_remove(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user_list')


# Event functions

def event_list(request):
    events = Event.objects.all()
    return render(request, 'api/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'api/event_detail.html', {'event': event})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('user_list')
    else:
        form = EventForm()
    return render(request, 'api/event_edit.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'api/event_edit.html', {'form': form})


def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('user_list')

# Query Functions

def search_user(request):
    user = ""
    users = ""
    form = UserSearchForm(request.POST)
    if form.is_valid():
        user = form.cleaned_data['username']
        users = User.objects.filter(username=user)
    return render(request, "api/user_search_form.html", {'form': form, 'user': user, 'users' : users})

def search_event(request):
    events = ""
    form = EventSearchForm(request.POST)
    if form.is_valid():
        event = form.cleaned_data['event_name']
        events = Event.objects.filter(event_name=event)
    return render(request, "api/event_search_form.html", {'form': form, 'events' : events})

def search_event_by_user(request):
    user = ""
    events = ""
    form = JoinSearchForm(request.POST)
    if form.is_valid():
        user_name = form.cleaned_data['username']
        user = User.objects.get(username = user_name)
        events = Event.objects.filter(event_name=user.event)
    return render(request, "api/join_search_form.html", {'form': form, 'events' : events})

def count_users_attending_event(request):
    event_name = ""
    users = ""
    num = 0
    form = AggregateSearchForm(request.POST)
    if form.is_valid():
        event_name = form.cleaned_data['event_name']
        users = User.objects.filter(event=event_name)
        for i in users:
            num = num + 1
    return render(request, "api/aggregate_search_form.html", {'form': form, 'event_name': event_name, 'users' : users, 'num': num})


def adventure(request):

        value = random.randint(0,3)
        places = ["Doak Campbell Stadium","Cascade Park", "Lake Ella","Sweet Shop"]
        description =""
        event_name = "Adventure Time"
        location = places[value]
        start_time = timezone.now()
        end_time = start_time + datetime.timedelta(seconds=random.randint(0, 86400))
        if(value == 0 ):
            description = "The finest stadium in all College Football, home to the Florida State Seminoles."
        elif(value == 1):
            description = "The biggest man-made park in all of Tallahasse. Enjoy the live music and scenery!"
        elif(value == 2):
            description = "Lake Ella is home to many shops and resturants and home to many types of ducks!"
        elif(value == 3):
            description = "At Sweet Shop you will be supporting one of the premier small buisnesses in Tallahasse, enjoy sweet treats and leave oyur mark by signning your name on the walls!"

        Event.objects.create(event_name=event_name,location=location,startTime=start_time,endTime=end_time)
        return render(request, 'api/adventure.html', {'end_time':end_time,'location':location,'start_time':start_time,'event_name':event_name,'description':description})




