from django.shortcuts import render
from django.views.generic import ListView
from users.models import Customer

class ListCustomers(ListView):
	model = Customer
	paginate_by = 10