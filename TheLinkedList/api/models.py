from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # User provides username, first_name, password
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default_png', upload_to='profile_pictures')
    follows = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.User.username


class Calendar(models.Model):
    COLOR_CHOICES = [
        ('RED', 'RED'),
        ('ORG', 'ORANGE'),
        ('YEL', 'YELLOW'),
        ('GRN', 'GREEN'),
        ('CYN', 'CYAN'),
        ('BLU', 'BLUE'),
        ('IND', 'INDIGO'),
        ('VIO', 'VIOLET'),
        ('GRY', 'GREY'),
        ('WHT', 'WHITE'),
    ]
    c_name = models.CharField(max_length=50, blank=False, null=False)
    color = models.CharField(max_length=3, choices=COLOR_CHOICES, default='RED')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s's Calendar: %s" % self.User.username, self.c_name


class Event(models.Model):
    # django automatically creates and stores id attribute
    e_name = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    startTime = models.DateTimeField(blank=False, null=False)
    endTime = models.DateTimeField(blank=False, null=False)
    belongs_to = models.ForeignKey(Calendar, blank=False, null=False)
    owner = models.ForeignKey(User, blank=False, null=False)