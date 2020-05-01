# imports
import json

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model

from events import models as event_models

User = get_user_model()

# End: imports -----------------------------------------------------------------

DATE_FORMATS = [
    "%d-%m-%y", "%d-%m-%Y", # 26-02-97  26-02-1997
    "%d/%m/%y", "%d/%m/%Y", # 26/02/97  26/02/1997
    "%d:%m:%y", "%d:%m:%Y", # 26:02:97  26:02:1997
    "%d.%m.%y", "%d.%m.%Y", # 26.02.97  26.02.1997
    "%d,%m,%y", "%d,%m,%Y", # 26,02,97  26,02,1997

    "%d/%m-%y", "%d/%m-%Y", # 26/02-97  26/02-1997
    "%d %m %y", "%d %m %Y", # 26 02 97  26 02 1997
]

TIME_FORMATS = [
    '%H:%M',        # '14:30'
    '%H.%M',        # '14.30'
    '%H %M',        # '14 30'
]

MIN_FORMATS = [
    "%M"
]

class EventForm(forms.ModelForm):

    required_css_class = 'required font-bold'

    class Meta:
        model = event_models.Event
        fields = [
            'title',
            'place',
            'start',
            'end',
            'description',
            'facebook_url',
            'image_url',
            # 'earlybirds',
            # 'price',
            # 'earlybird_price',
        ]

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # self.fields['title'].widget.attrs.update({'placeholder': 'Tittel'})

        self.fields['start'].widget.attrs.update({'class': 'flatpickr form-control'})
        self.fields['end'].widget.attrs.update({'class': 'flatpickr form-control'})
        self.fields['description'].widget.attrs.update({'class': 'tinymce form-control'})
        # self.fields['start'].widget.format = "%H:%M"
        #
        # self.fields['date'].widget.attrs.update({'placeholder': 'dd.mm.yy'})
        # self.fields['date'].widget.format = "%d.%m.%y"
        #
        # self.fields['end'].widget.attrs.update({'placeholder': 'hh:mm'})
        # self.fields['end'].widget.format = "%H:%M"
        




class EventFilterForm(forms.Form):
    search = forms.CharField(required=False, label="Søk")
    tag = forms.ChoiceField(required=False)
    # tag = forms.ChoiceField(required=False)
    lead = forms.ChoiceField(required=False, label="Instruktør (lead)")
    # lead = forms.ChoiceField(required=False, label="Instruktør (lead)")
    follow = forms.ChoiceField(required=False, label="Instruktør (follow)")
    bulk = forms.IntegerField(required=False, label="Bolk")
    day = forms.IntegerField(required=False, label="Dag")
    semester_char = forms.CharField(required=False, label="Semester")

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields:
            # pass
            self.fields[field].widget.attrs.update({'class': 'event-filter form-control'})

        self.fields['search'].widget.attrs.update({'placeholder': 'Søk på tittel...', 'autofocus': True})
        self.fields['semester_char'].widget.attrs.update({'placeholder': 'Eks: H2019, V2020',})

        # self.fields['tag'].choices = [(-1, '-----')]
        # self.fields['tag'].choices += [(tag.id, tag.title) for tag in song_models.Tag.getQueryset(["event"])]
        # self.fields['tag'].widget.attrs.update({'class': 'form-control event-filter'})
