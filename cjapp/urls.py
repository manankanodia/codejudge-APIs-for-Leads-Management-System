"""cjapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
# from restapi.views import *


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]


# from django.urls import path
#
# from restapi.views import *
#
# urlpatterns = [
#     path('api/leads/<int:id>', get_lead),
#     path('api/leads/', generate_lead),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    path('api/leads/<int:pk>', views.Leads.as_view()),
    path('api/leads/', views.Leads.as_view()),
    path('api/mark_lead/<int:pk>', views.MarkLead.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
