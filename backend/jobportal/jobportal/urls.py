"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('recruiter',views.RecruiterRegisterView,basename='reg_view'),
router.register('user',views.UserRegisterView,basename='user_view'),
router.register('jobposter',views.JobPostViewSet,basename='job_view'),
router.register('saved/list',views.SavedJobListView,basename='saved_modelview'),


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),
     path('token/generate',obtain_auth_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)