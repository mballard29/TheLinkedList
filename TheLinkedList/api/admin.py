from django.contrib import admin
from .models import Profile, Calendar, Event

admin.site.register(Profile)
admin.site.register(Calendar)
admin.site.register(Event)