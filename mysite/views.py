from django.shortcuts import render
from mysite.models import *

def home(request):
	student = Student.objects.filter(id__gt=1)
	return render(request, 'home.html', {'student':student})