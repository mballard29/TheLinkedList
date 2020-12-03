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

# class AdventureForm(forms.ModelForm):
#        class Meta:
#            model = Event
#            fields = ('event_name', 'location', 'startTime', 'endTime', 'description')





# no InviteCreationForm or InviteDeletionForm yet since this should be managed with the event forms