# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import *


# urls for the app to bind templates and views
urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_entry/$', add_entry, name='add_entry'),
	url(r'^predict/$', predict, name='predict')
]