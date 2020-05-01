"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views

from django.contrib.auth import get_user_model
User = get_user_model()



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('forbidden/', TemplateView.as_view(template_name="main/forbidden.html"), name='forbidden'),
    path('admin/', admin.site.urls),
    path('lyche/', include('lyche.urls')),
    path('arrangementer/', include('events.urls')),
    path('informasjon/', include('info.urls')),
    path('accounts/', include('accounts.urls')),
    path('opptak/', include('recruitment.urls')),
    path('gallery/', include('gallery.urls')),

    # path('api/users/', emil_api.ExtendedAPI.as_view(model=User), name="api_users"),
    # path('api/workouts/', emil_api.ExtendedAPI.as_view(model=emil_models.Workout), name="api_workouts"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
