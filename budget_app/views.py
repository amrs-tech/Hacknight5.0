# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel, BudgetEntryModel


# Create your views here.
def index(request):
	"""
	Index view to display login/signup page
	"""
	if request.method == 'POST':
		print request.POST.get('name')
		print request.POST.get('password')
		u = UserModel()
		u.name = request.POST.get('name')
		u.email = request.POST.get('email')
		u.password = request.POST.get('password')
		u.save()

	return render(request, 'signup.html')


def predict(request):
	if len(BudgetEntryModel.objects.all()):
		# ml model run
		print 'ml'
		pass
	return render(request, 'new_entry.html')


def add_entry(request):
	"""
	View to add new budget entries
	"""
	if request.method == 'POST':
		b = BudgetEntryModel()
		b.purpose = request.POST.get('purpose')
		b.price = request.POST.get('price')
		if request.POST.get('date'):
			b.date_of_expenditure = request.POST.get('date')
		b.save()

	return render(request, 'predict.html')
