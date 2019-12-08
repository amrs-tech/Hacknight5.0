# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserModel(models.Model):
	# Model to store user signup details
	email = models.EmailField()
	name = models.CharField(max_length=250)
	password = models.CharField(max_length=20)

	class Meta:
		app_label = "budget_app"

	def __str__(self):
		return self.name



class BudgetEntryModel(models.Model):
	# Model to store the budget entries of each users
	# user = ForeignKey(UserModel)
	purpose = models.CharField(max_length=200)
	price = models.FloatField()
	date_of_expenditure = models.DateField()

	class Meta:
		app_label = "budget_app"

	def __str__(self):
		try:
			return self.id
		except:
			return self.purpose
