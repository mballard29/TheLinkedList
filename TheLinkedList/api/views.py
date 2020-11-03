from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Profile, Calendar, Event, Invite
# from .models import FriendRequest
# from feed.models import Post
from .forms import UserRegisterForm, UserUpdateForm
import random


User = get_user_model()


@login_required
def my_profile(request):
    p = request.user.profile
    you = p.user
    user_calendars = Calendar.objects.filter(owner=you)

    context = {
        'u': you,
        'calendar_count': user_calendars.count
    }

    return render(request, 'users/profile.html', context)

