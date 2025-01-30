from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Concert(models.Model):
    # concert_name: CharField with max_length of 255
    concert_name = models.CharField(max_length=255)
    # duration: IntegerField
    duration = models.IntegerField()
    # city: CharField with max_length of 255
    city = models.CharField(max_length=255)
    # date: DateField with the default time of now
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.concert_name


class ConcertAttending(models.Model):
    class AttendingChoices(models.TextChoices):
        NOTHING = "-", _("-")
        NOT_ATTENDING = "Not Attending", _("Not Attending")
        ATTENDING = "Attending", _("Attending")

    concert = models.ForeignKey(
        Concert, null=True, on_delete=models.CASCADE, related_name="attendees"
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    attending = models.CharField(
        max_length=100,
        choices=AttendingChoices.choices,
        default=AttendingChoices.NOTHING,
    )

    class Meta:
        unique_together = ['concert', 'user']

    def __str__(self):
        return self.attending


class Photo(models.Model):
    # id: IntegerField as a primary key
    id = models.IntegerField(primary_key=True)
    # pic_url: CharField with max_length of 1000
    pic_url = models.CharField(max_length=1000)
    # event_country: CharField with max_length of 255
    event_country = models.CharField(max_length=255)
    # event_state: CharField with max_length of 255
    event_state = models.CharField(max_length=255)
    # event_city: CharField with max_length of 255
    event_city = models.CharField(max_length=255)
    # event_date: DateField with the default time of now
    event_date = models.DateField(default=timezone.now)

    class Meta:
        managed = False

    def __str__(self):
        return self.pic_url


class Song(models.Model):
    # id: IntegerField as a primary key
    id = models.IntegerField(primary_key=True)
    # title: CharField with max_length of 255
    title = models.CharField(max_length=255)
    # lyrics: TextField
    lyrics = models.TextField()

    class Meta:
        managed = False

    def __str__(self):
        return self.title
