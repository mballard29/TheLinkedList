from django.db import models


# Create your models here.
class User(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=128)
    uname = models.CharField(max_length=128)
    profile_picture = models.CharField(max_length=1000)

class Calendar(models.Model):
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    cal_name = models.CharField(max_length=100)

class Colors(models.Model):
    option = models.CharField(max_length=50)

class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_on = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    ccoded = models.ForeignKey(Colors, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    location = models.CharField(max_length=250)
    startDateTime = models.DateTimeField(max_length=250)
    endDateTime = models.DateTimeField(max_length=250)
    description = models.CharField(max_length=1000)