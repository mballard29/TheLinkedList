from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Calendar, Event, Invite
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CalendarCreationForm, CalendarUpdateForm, EventCreationForm, EventUpdateForm

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in!')
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request, slug):
    p = Profile.objects.filter(slug=slug).first()
    u = p.owner
    users_calendars = Calendar.objects.filter(owner=u)
    follows = p.follows.all()

    # is this user our friend
    button_status = 'none'
    if p not in request.user.profile.follows.all():
        button_status = 'not_following'

    context = {
        'u': u,
        'button_status': button_status,
        'follows_list': follows,
        'calendar_count': users_calendars.count
    }

    return render(request, "profile.html", context)


@login_required
def my_profile(request):
    p = request.user.profile
    you = p.owner
    users_calendars = Calendar.objects.filter(owner=you)
    follows = p.follows.all()

    # my profile will say 'edit my profile' instead of following status
    button_status = 'none'

    context = {
        'u': you,
        'button_status': button_status,
        'follows_list': follows,
        'calendar_count': users_calendars.count
    }

    return render(request, "profile.html", context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('my_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'edit_profile.html', context)


@login_required
def search_users(request):
    query = request.GET.get('q')
    object_list = User.objects.filter(username__icontains=query)
    context = {
        'users': object_list
    }
    return render(request, "search_users.html", context)


'''
testing event requests


@login_required
def send_event_invite(request, id):
    # puts event invite into Invite table
    # send invite to user with user.id = id
    to_user = get_object_or_404(User, id=id)
    evinvite, created = Invite.objects.get_or_create(
        from_user=request.user,
        to_user=to_user,
        event=request.event,
    )
    return HttpResponseRedirect('/users/{}'.format(to_user.profile.slug))

@login_required
def accept_event_invite(request, id):
    # removes event invite from Invite table
    # adds to_user to event.invited
    from_user = get_object_or_404(User, id=id)
    evinvite = Invite.objects.filter(from_user=from_user, to_user=request.user).first()
    from_user = get_object_or_404(User, id=id)
    evinvite = Invite.objects.filter(from_user=from_user, to_user=request.user).first()
    event = Event.object.filter(id=evinvite.event.id)
    event.invited.add(evinvite.to_user.profile)

    evinvite.delete()
    return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))


@login_required
def reject_event_invite(request, id):
    from_user = get_object_or_404(User, id=id)
    evinvite = Invite.objects.filter(from_user=from_user, to_user=request.user).first()
    evinvite.delete()
    return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))


@login_required
def cancel_friend_request(request, id):
    user = get_object_or_404(User, id=id)
    evinvite = Invite.objects.filter(from_user=request.user, to_user=user).first()
    evinvite.delete()
    return HttpResponseRedirect('/users/{}'.format(user.profile.slug))
    
    
'''

'''
add later
    views/functions for sending, accepting, and cancelling event invites
    views/functions for deleting events
    views/functions for deleting calendars - make it so you can't delete 'shared events'
'''

'''
these views reference (to be made later) in api > templates > api 
    register.html
    profile.html
    edit_profile.html
    search_users.html
'''