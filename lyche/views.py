# # imports
import os
import json
import datetime

from django.views import View
from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from lyche import forms as lyche_forms
from lyche import models as lyche_models

User = get_user_model()

# End: imports -----------------------------------------------------------------


perms_example = [
    login_required,
    permission_required('lyche.view_examplemodel', login_url='lyche:forbidden')
]
@method_decorator(perms_example, name='dispatch')
class AllExampleModels(View):
    template = 'lyche/all_examplemodels.html'

    def get(self, request):
        examplemodels = lyche_models.ExampleModel.objects.all()
        return render(request, self.template, {
            'examplemodels': examplemodels,
        })



class AddExampleModel(main_views.GenericAddModel):
    # template = 'lyche/quotation_form.html'
    form_class = lyche_forms.ExampleForm
    redirect_name = 'lyche:add_examplemodels'
    debug = 2



class EditExampleModel(main_views.GenericEditModel):
    # template = 'lyche/quotation_form.html'
    form_class = lyche_forms.ExampleForm
    redirect_name = 'lyche:all_examplemodels'
    model = lyche_models.Quotation
    debug = 2
