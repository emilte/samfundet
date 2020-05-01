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

from skeleton import forms as skeleton_forms
from skeleton import models as skeleton_models

User = get_user_model()

# End: imports -----------------------------------------------------------------


perms_example = [
    login_required,
    permission_required('skeleton.view_examplemodel', login_url='skeleton:forbidden')
]
@method_decorator(perms_example, name='dispatch')
class AllExampleModels(View):
    template = 'skeleton/all_examplemodels.html'

    def get(self, request):
        examplemodels = skeleton_models.ExampleModel.objects.all()
        return render(request, self.template, {
            'examplemodels': examplemodels,
        })



class AddExampleModel(main_views.GenericAddModel):
    # template = 'skeleton/quotation_form.html'
    form_class = skeleton_forms.ExampleForm
    redirect_name = 'skeleton:add_examplemodels'
    debug = 2



class EditExampleModel(main_views.GenericEditModel):
    # template = 'skeleton/quotation_form.html'
    form_class = skeleton_forms.ExampleForm
    redirect_name = 'skeleton:all_examplemodels'
    model = skeleton_models.Quotation
    debug = 2
