"""django_react_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from students import views
#from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/students/$', views.students_list),
    re_path(r'^api/students/([0-1000])$', views.students_detail),
    re_path(r'^api/classroom/$', views.classroom_list),
    re_path(r'^api/classroom/([0-1000])$', views.classroom_detail),
    path('api-auth/', include('rest_framework.urls')),
]

#test of git

#test of git2