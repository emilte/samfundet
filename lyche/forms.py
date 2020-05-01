# # imports
import json

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from lyche import models as lyche_models

from django.contrib.auth import get_user_model
User = get_user_model()
# End: imports -----------------------------------------------------------------

class ExampleForm(forms.ModelForm):

    required_css_class = 'required font-bold' # Space-separated classes added to required fields in templates

    class Meta:
        model = lyche_models.ExampleModel # Form uses fields from model and enables form.save()
        # fields or excludes is required
        fields = [] # list of fields (field-name as string) allowed in form.
        excludes = [] # list of fields (field-name as string) disallowed in form. (All other fields automatically included)


    # Override init method to modify fields etc.
    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'}) # Example of how bootstrap class is added to every field

        # Explicitly targeted field
        self.fields['example_field'].widget.attrs.update({'class': 'example-class'})


# Normal form instead of ModelForm
# Fields must be defined here
class ExampleForm2(forms.Form):
    form2_char = forms.CharField(required=False, label="Char2")
    form2_choice = forms.ChoiceField(required=False, choices=[])
    form2_int = forms.IntegerField(required=False, label="Int2")

    required_css_class = 'required font-bold'

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
