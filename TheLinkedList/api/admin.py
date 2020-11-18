from django.contrib import admin
from .models import Profile, Calendar, Event, Invite

admin.site.register(Profile)
admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(Invite)

