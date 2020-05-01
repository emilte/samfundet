# import json
# import inspect
#
# from django.views import View
# from django.http.response import JsonResponse
# from django.http import HttpResponse, HttpResponseBadRequest
#
# from skeleton import models as skeleton_models
#
# import logging
# logger = logging.getLogger(__name__)
#
# # Get custom User from settings.AUTH_USER_MODEL
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
#
# # Views that doesn't return templates
# # Can be used as api getting and posting data
#
# class ExampleAPI(View):
#
#     def post(self, request):
#         try:
#             id = request.POST.get('id', None)
#             examplemodel = skeleton_models.ExampleModel.objects.filter(id=id).first()
#             if examplemodel:
#                 pass # Do something
#         except Exception as e:
#             return HttpResponse(status=404) # Not found
#
#         # Return data as json
#         return JsonResponse(status=200, data={
#             'examplemodel': examplemodel,
#         }) # OK
