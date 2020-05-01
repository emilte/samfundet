# # imports
from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()
# # End: imports -----------------------------------------------------------------


class ExampleModel(models.Model):
    title = models.CharField(null=True, blank=False, max_length=100, unique=True, verbose_name="Tittel")
    image = models.ImageField(upload_to="img", null=True, blank=True, verbose_name="Bilde")
    file = models.FileField(upload_to="file", null=True, blank=True, verbose_name="Fil")
    description = models.TextField(null=True, blank=True, verbose_name="Beskrivelse")
    tags = models.ManyToManyField('gallery.Tag', blank=True, related_name="uploads")
    datetime = models.DateTimeField(null=True, blank=True, verbose_name="Tidspunkt")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="quotations", verbose_name="Bruker")

    class Meta:
        ordering = ['-title']
        verbose_name = "Eksempel"
        verbose_name_plural = "Eksempler"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    @staticmethod
    def get_images():
        return Upload.objects.exclude(image__exact='')

    # Normal instance method
    def is_favorited_by(self, user):
        return self.favorites.filter(id=user.id).exists()

    # Class method
