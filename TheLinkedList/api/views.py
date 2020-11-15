from django.http import HttpResponse, HttpResponseRedirect
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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login!')
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


@login_required
def my_profile(request):
    p = request.user.profile
    you = p.owner
    user_calendars = Calendar.objects.filter(owner=you)

    context = {
        'u': you,
        'calendar_count': user_calendars.count
    }

    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('my_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }
    return render(request, 'users/edit_profile.html', context)


@login_required
def profile_view(request, slug):
    p = Profile.objects.filter(slug=slug).first()
    u = p.owner
    user_calendars = Calendar.objects.filter(owner=u)

    follows = p.follows.all()

    # is this user our friend
    button_status = 'none'
    if p not in request.user.profile.follows.all():
        button_status = 'not_friend'

    context = {
        'u': u,
        'button_status': button_status,
        'follows_list': follows,
        'calendar_count': user_calendars.count
    }

    return render(request, "users/profile.html", context)


def friend_list(request):
    p = request.user.profile
    follows = p.follows.all()

    context = {
        'follows_list': follows
    }

    return render(request, "users/friend_list.html", context)


@login_required
def search_users(request):
    query = request.GET.get('q')
    object_list = User.objects.filter(username__icontains=query)

    context = {
        'users': object_list
    }
    return render(request, "users/search_users.html", context)


# will not do the right thing yet
# def delete_friend(request, id):
#     user_profile = request.user.profile
#     follow_profile = get_object_or_404(Profile, id=id)
#     user_profile.follows.remove(follow_profile)
#     return HttpResponseRedirect('/users/{}'.format(follow_profile.slug))
#
#
# @login_required
# def send_event_request(request, id):
#     user = get_object_or_404(User, id=id)
#     erequest, created = Invite.objects.get_or_create(from_user=request.user, to_user=user)
#     return HttpResponseRedirect('/users/{}'.format(user.profile.slug))
#
#
# @login_required
# def cancel_event_request(request, id):
#     user = get_object_or_404(User, id=id)
#     erequest = Invite.objects.filter(from_user=request.user, to_user=user).first()
#     erequest.delete()
#     return HttpResponseRedirect('/users/{}'.format(user.profile.slug))
#
#
# @login_required
# def accept_event_request(request, id):
#     from_user = get_object_or_404(User, id=id)
#     erequest = Invite.objects.filter(from_user=from_user, to_user=request.user).first()
#     user1 = erequest.to_user
#     user2 = from_user
#     return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))
#
#
# @login_required
# def delete_event_request(request, id):
#     from_user = get_object_or_404(User, id=id)
#     erequest = Invite.objects.filter(from_user=from_user, to_user=request.user).first()
#     erequest.delete()
#     return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))


'''
send_event_request
cancel_event_request
accept_event_request
delete_event_request

'''
