# imports
import os
import json
import datetime

from django.views import View
from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from main import views as main_views
from events import forms as event_forms
from events import models as event_models
from accounts import models as account_models

from django.contrib.auth import get_user_model
User = get_user_model()

# End: imports -----------------------------------------------------------------

# Functions
def trace(x):
    print(json.dumps(x, indent=4, sort_keys=True))

# End: Functions ---------------------------------------------------------------

perms_add_event = [
    login_required,
    permission_required('events.add_event', login_url='forbidden')
]
@method_decorator(perms_add_event, name='dispatch')
class AddEventView(main_views.GenericAddModel):
    template = 'events/event_form.html'
    form_class = event_forms.EventForm
    redirect_name = 'events:all_events'
    #redirect_id = 'id'


editEvent_dec = [
    login_required,
    permission_required('events.change_event', login_url='forbidden')
]
class EditEventView(main_views.GenericEditModel):
    template = 'events/event_form.html'
    form_class = event_forms.EventForm
    redirect_name = 'events:event_view'
    redirect_id = 'id'
    model = event_models.Event



allEvents_dec = [
    login_required,
    # permission_required('events.view_event', login_url='forbidden')
]
@method_decorator(allEvents_dec, name='dispatch')
class AllEventsView(View):
    template = 'events/all_events.html'
    form = event_forms.EventFilterForm

    def get(self, request):
        events = event_models.Event.objects.all()
        form = self.form()
        return render(request, self.template, {'form': form, 'events': events})

    def post(self, request):
        events = event_models.Event.objects.all()
        form = self.form(data=request.POST)
        if form.is_valid():
            events = self.event_filter(form, events)
        return render(request, self.template, {'form': form, 'events': events})

    def event_filter(self, form, queryset):
        search = form.cleaned_data['search']
        tag = form.cleaned_data['tag'] or None
        lead = form.cleaned_data['lead'] or None
        follow = form.cleaned_data['follow'] or None
        bulk = form.cleaned_data['bulk']
        day = form.cleaned_data['day']
        semester_char = form.cleaned_data['semester_char']

        if search != "":
            queryset = queryset.filter(title__icontains=search)
        if tag:
            queryset = queryset.filter(tags__id=tag)
        if lead:
            queryset = queryset.filter(lead=lead)
        if follow:
            queryset = queryset.filter(follow=follow)
        if bulk:
            queryset = queryset.filter(bulk=bulk)
        if day:
            queryset = queryset.filter(day=day)
        if semester_char:
            queryset = queryset.filter(semester_char=semester_char)

        return queryset



event_dec = [
    login_required,
    # permission_required('events.view_event', login_url='forbidden')
]
@method_decorator(event_dec, name='dispatch')
class EventView(View):
    template = 'events/event_view.html'

    def get(self, request, eventID):
        event = event_models.Event.objects.get(id=eventID)
        return render(request, self.template, {'event': event})



signup_dec = [
    login_required,
    # permission_required('events.view_event', login_url='forbidden')
]
@method_decorator(signup_dec, name='dispatch')
class EventSignup(View):

    def post(self, request, modelID):
        event = event_models.Event.objects.get(id=modelID)
        p, created = event_models.Participant.objects.get_or_create(
            user=request.user,
            event=event,
        )

        return redirect("events:event_view", modelID)
