from django.contrib import admin
# from .models import Profile, Calendar, Event, Invite
from .models import User, Event

admin.site.register(User)
admin.site.register(Event)
# admin.site.register(Calendar)
# admin.site.register(Invite)

