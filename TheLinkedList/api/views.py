from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.base import View

from .forms import UserRegisterForm
from .models import Profile, Calendar, Event, Invite
from .forms import UserUpdateForm, ProfileUpdateForm, CalendarCreationForm, CalendarUpdateForm, EventCreationForm, \
    EventUpdateForm

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


class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'register.html'


# Displays blank form
def get(self, request):
    form = self.form_class(None)
    return render(request, self.template_name, {'form': form})


# process login request
def post(self, request):
    form = self.form_class(request.POST)

    if form.is_valid():
            #doesnt save into database yet

            user = form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                        login(request,user)
                        return redirect('profile.html')


         #   return render(request, self.template_name, {'form': form} )
#testing


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
