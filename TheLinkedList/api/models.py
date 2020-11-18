from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from autoslug import AutoSlugField


# class User(contrib.auth.models)


class Profile(models.Model):
    # User provides username, first_name, password
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pic', blank=True, null=False)
    slug = AutoSlugField(populate_from='user')
    follows = models.ManyToManyField('self', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.User.username

    def get_absolute_url(self):
        return '/users/{}'.format(self.slug)


def post_save_user_model_reciever(sender, instance, created, *args, **kwargs):
    """ creates profile as soon as user creates account """
    if created:
        try:
            u = Profile.objects.create(user=instance)
            Calendar.objects.create(c_name='Shared Events', color='YEL', owner=u)
        except:
            pass


post_save.connect(post_save_user_model_reciever, sender=settings.AUTH_USER_MODEL)


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
    color = models.CharField(max_length=3, choices=COLOR_CHOICES, default='RED', blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s's Calendar: %s" % self.User.username, self.c_name


class Event(models.Model):
    # django automatically creates and stores id attribute
    e_name = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    startTime = models.DateTimeField(blank=False, null=False)
    endTime = models.DateTimeField(blank=False, null=False)
    # who created this event
    belongs_to = models.ForeignKey(Calendar, on_delete=models.CASCADE, blank=False, null=False)
    # who is invited to this event
    invited = models.ManyToManyField(Profile, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s's Event: %s" % self.User.username, self.e_name


class Invite(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Event %s invited %s" % self.event.e_name, self.to_user.username