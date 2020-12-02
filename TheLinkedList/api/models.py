from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # event = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Event(models.Model):
    e_name = models.CharField(max_length=20)
    location = models.CharField(max_length=50, default="")
    startTime = models.DateTimeField(default = timezone.now,blank=False, null=False)
    endTime = models.DateTimeField(default = timezone.now,blank=False, null=False)
    description = models.TextField(default="")
    # belongs_to = models.ForeignKey(Calendar, on_delete=models.CASCADE, blank=False, null=False)
    # invited = models.ManyToManyField(Profile, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.e_name


# class Invite(models.Model):
#     from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "Event %s invited %s" % self.event.e_name, self.to_user.username