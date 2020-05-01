from django.views import View
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import models as auth_models

from accounts import models as account_models
# Create your views here.

class Home(View):
    template = 'main/home.html'

    def get(self, request):
        groups = auth_models.Group.objects.all()
        departments = account_models.Department.objects.all()
        return render(request, self.template, {
            'groups': groups,
            'departments': departments,
        })


class GenericAddModel(View):
    template = "main/generic_form.html"
    form_class = None # (*) Required
    redirect_name = None # (*)
    redirect_id = None
    success_msg = "Lagringen var vellykket!"
    error_msg = "Lagringen var misslykket!"
    debug = 0 # [0, 1, 2, 3] higher lvl equals more detailed debug
    _cn = None

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self._cn = self.__class__.__name__

        if not self.form_class:
            raise RuntimeError("Attribute 'form_class' is required")
        if not self.redirect_name:
            raise RuntimeError("Attribute 'redirect_name' is required")

        if self.debug >= 1:
            print(f"== debug: activated from {self._cn} ==")
        if self.debug >= 2:
            print(f"== __init__: form_class = {self.form_class.__name__}")
            print(f"== __init__: template = {self.template}")
            print(f"== __init__: redirect_name = {self.redirect_name}")
            print(f"== __init__: redirect_id = {self.redirect_id}")
            print(f"== __init__: success_msg = {self.success_msg}")
            print(f"== __init__: error_msg = {self.error_msg}")

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request, form=None):
        if not form:
            form = self.form_class(request.POST, request.FILES)

        if self.debug >= 1:
            print(f"== {self._cn}.post: form = {form.data}\n\n")
            print(f"== {self._cn}.post: form.is_valid() = {form.is_valid()}")

        if form.is_valid():
            obj = form.save(commit=False)

            try:
                obj.creator = request.user
            except Exception as e:
                if self.debug >= 2: print(e)

            try:
                obj.created = timezone.now()
            except Exception as e:
                if self.debug >= 2: print(e)

            try:
                obj.last_editor = request.user
            except Exception as e:
                if self.debug >= 2: print(e)


            try:
                obj.last_edited = timezone.now()
            except Exception as e:
                if self.debug >= 2: print(e)

            # Save
            obj.save()

            try:
                form.save_m2m()
            except Exception as e:
                if self.debug >= 2: print(e)

            messages.success(request, self.success_msg)

            if self.redirect_id:
                return redirect(self.redirect_name, getattr(obj, self.redirect_id))
            else:
                return redirect(self.redirect_name)
        else:
            messages.error(request, self.error_msg)
            return render(request, self.template, {'form': form})


class GenericEditModel(GenericAddModel):
    model = None # Required

    def __init__(self, *args, **kwargs):
        super(GenericAddModel, self).__init__(*args, **kwargs)

        if not self.model:
            raise RuntimeError("Attribute 'model' is required")

    def get(self, request, modelID):
        instance = self.model.objects.get(id=modelID)
        form = self.form_class(instance=instance)
        return render(request, self.template, {'form': form, 'modelID': modelID})

    def post(self, request, modelID):
        instance = self.model.objects.get(id=modelID)
        form = self.form_class(request.POST, request.FILES, instance=instance)
        return super().post(request, form)








        # if form.is_valid():
        #     instance = form.save(commit=False)
        #     try:
        #         instance.last_editor = request.user
        #         instance.last_edited = timezone.now()
        #     except Exception as e:
        #         print(e)
        #     finally:
        #         instance.save()
        #
        #     messages.success(request, self.success_msg)
        #
        #     if self.redirect_id:
        #         return redirect(self.redirect_name, getattr(instance, self.redirect_id))
        #     else:
        #         return redirect(self.redirect_name)
        # else:
        #     messages.error(request, self.error_msg)
        #     return render(request, self.template, {'form': form, 'modelID': modelID})
