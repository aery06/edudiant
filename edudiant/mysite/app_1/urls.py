# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
#        url(r'', views.index, name = 'index'),
        url(r'^index$', views.index, name = 'index'),
        url(r'^connection$', views.connection, name = 'connection'),
         url(r'^default$', views.index, name = 'default'),
         url(r'^resources$', views.resources, name = 'resources'),
         url(r'^vedios$', views.vedios, name = 'vedios'),
         url(r'^audio$', views.audio, name = 'audio'),
          url(r'^docs$', views.docs, name = 'docs'),
            ];