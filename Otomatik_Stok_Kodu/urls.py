"""Otomatik_Stok_Kodu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from stok.views import UserViewSet, GroupViewSet
from stok.views import *
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from stok.views import approve_stok
from django.conf.urls import url, include
""" REST API """

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView ),
    path('login/',LoginPageView),
    path('logout/',logoutUser, name="logout"),
    path('stockrequest/',StockRequestView),
    path('stocklist/',StockListView),
    path('stockapprovelist',StockApprovalView),
    path(r'', include("river_admin.urls")),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include ("river_admin.urls")),

    
    url(r'^approve_stok/(?P<stok_id>\d+)/(?P<next_state_id>\d+)/$', approve_stok, name='approve_stok'),

]

