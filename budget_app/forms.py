# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import UserModel


# Forms for the app
class UserForm(forms.ModelForm):
	"""
	Form inherits the UserModel fields
	"""
	class Meta:
		model = UserModel
		fields = "__all__"