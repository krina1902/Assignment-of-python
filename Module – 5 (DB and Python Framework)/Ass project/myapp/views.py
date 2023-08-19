from django.shortcuts import render
from .models import Admin,Productmanager

# Create your views here.


def index(request):

	if request.method=='POST':
		Admin.objects.create(
			
			product_name=request.POST['product_name'],
			product_id=request.POST['product_id'],
			
			)
		msg='Product Added Successfully'
		return render(request,'index.html',{'msg':msg})
	else:
		return render(request,'index.html')