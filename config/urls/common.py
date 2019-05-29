# config/urls/common.py
"""Admin_Epg_Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from apps.core.routers import router

API_TITLE = 'Admin_Epg_Api'
API_DESCRIPTION = '...'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        r'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    path(
        r'docs/',
        include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path(r'api/', include((router.urls, 'api_v1'), namespace='api_v1')),
    path(r'api/login/', obtain_jwt_token),
    path(r'api/token-verify/', verify_jwt_token),
    path(r'api/refresh-token/', refresh_jwt_token),
]
