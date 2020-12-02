from django import forms
from .models import User, Event
# from django.contrib.auth.models import User
# from .models import Profile, Calendar, Event, Invite
# from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'event',)

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('event_name', 'location', 'startTime', 'endTime', 'description',)

class UserSearchForm(forms.Form):
	username = forms.CharField(label='username', max_length=20)

class EventSearchForm(forms.Form):
	event_name = forms.CharField(label='event_name', max_length=20)

class JoinSearchForm(forms.Form):
	username = forms.CharField(label='username', max_length=20)

class AggregateSearchForm(forms.Form):
	event_name = forms.CharField(label='event_name', max_length=20)


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_pic']


# class CalendarCreationForm(forms.ModelForm):
#     class Meta:
#         model = Calendar
#         fields = ['c_name', 'color']
#         # color is chosen from a select number of choices, ideally a drop down menu


# class CalendarUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Calendar
#         fields = ['c_name', 'color']


# class EventCreationForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['e_name', 'location', 'startTime', 'endTime', 'description']
#         # location is just a string right now
#         # startTime, endTime is a DateTime field
#         # description is a (CharField) text field
#         # maybe add invited to fields; dynamic search bar to add who is invited


# class EventUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['e_name', 'location', 'startTime', 'endTime', 'description']


# no InviteCreationForm or InviteDeletionForm yet since this should be managed with the event forms