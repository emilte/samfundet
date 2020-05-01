# imports
from django.db import models
from django.conf import settings
from django.utils import timezone

from main import base as main_base

# End: imports -----------------------------------------------------------------

# Intermediate model
class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Bruker")
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, null=False, blank=False, verbose_name="Event")
    date_joined = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Dato påmeldt")
    has_paid = models.BooleanField(default=False, verbose_name="Har betalt")

    class Meta:
        ordering = ['id']
        verbose_name = "Deltaker"
        verbose_name_plural = "Deltakere"

    def __str__(self):
        return f"Participant: {self.user}"

class Event(main_base.CustomBaseModel):
    title = models.CharField(max_length=140, null=True, blank=False, verbose_name="Tittel")
    place = models.CharField(max_length=140, null=True, blank=True, verbose_name="Sted")
    start = models.DateTimeField(null=True, blank=True, verbose_name="Start")
    end = models.DateTimeField(null=True, blank=True, verbose_name="Slutt")
    description = models.TextField(null=True, blank=True, verbose_name="Beskrivelse")
    facebook_url = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)


    # price = models.IntegerField(null=True, blank=True)

    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through='events.Participant', blank=True, related_name="events", verbose_name="Påmeldte")


    class Meta:
        ordering = ['-start', 'title']
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.title}"
        # return "{} ({})".format(self.getTitle(), self.getDate())

    def save(self, *args, **kwargs):
        return super(Event, self).save(*args, **kwargs)
