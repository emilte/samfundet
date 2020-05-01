# imports
from django.urls import path
from django.views.generic import TemplateView

from lyche import views
from lyche import api
# End: imports -----------------------------------------------------------------

app_name = 'lyche'

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path('example/all/', views.AllExampleModels.as_view(), name="all_examplemodels"),
    path('example/add/', views.AddExampleModel.as_view(), name="add_examplemodel"),
    path('example/edit/<int:modelID>/', views.EditExampleModel.as_view(), name="edit_examplemodel"),
    path('example/<int:modelID>/', views.ExampleModel.as_view(), name="view_examplemodel"),
    
]
