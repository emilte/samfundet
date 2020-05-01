# # imports
from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils import timezone

# # End: imports -----------------------------------------------------------------

# Base abstract classes

# Base admin with useful fields and save method
class CustomBaseAdmin(admin.ModelAdmin):
    readonly_fields = ['creator', 'created', 'last_edited', 'last_editor']

    def save_model(self, request, obj, form, change):
        try:
            if not change:
                obj.creator = request.user
                obj.created = timezone.now()
            obj.last_editor = request.user
            obj.last_edited = timezone.now()
        except Exception as e:
            pass

        return super().save_model(request, obj, form, change)


# Base model with useful fields and save method
class CustomBaseModel(models.Model):
    last_editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name="editor_%(class)s_set", verbose_name="Sist redigert av")
    last_edited = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Sist redigert")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name="creator_%(class)s_set", verbose_name="Opprettet av")
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Opprettet")

    class Meta:
        abstract = True

    # Creator and editor must be set in view. Model save-method doesn't know which user is saving
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_edited = timezone.now()
        return super().save(*args, **kwargs)
