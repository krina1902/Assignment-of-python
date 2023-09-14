from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from .models import User


def index(request):

	return render(request,'index.html')

def seller_index(request):
	return render(request,'seller-index.html')

def signup(request):
	
	if request.method=='POST':
		try:
			User.objects.get(email=request.POST['email'])
			msg='Email Already Registered'
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic'],
					usertype=request.POST['usertype'],
					admin_access=admin_access,
					)
				msg='SignUp Suceesfully'
				return render(request,'signup.html',{'msg':msg})
			else:
				msg='Password & Confirm Password Does Not Match'
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="buyer":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					wishlists=Wishlist.objects.filter(user=user)
					request.session['wishlist_count']=len(wishlists)
					carts=Cart.objects.filter(user=user,payment_status=False)
					request.session['cart_count']=len(carts)
					return redirect('index')
				else:
					if user.admin_access==True:
						request.session['email']=user.email
						request.session['fname']=user.fname
						request.session['profile_pic']=user.profile_pic.url
						return render(request,'seller-index.html')
					else:
						msg='Admin not accept your request'
						return render(request,'login.html',{'msg':msg})
			else:
				msg='Your Password is Incorrect'
				return render(request,'login.html',{'msg':msg})
		except:
			msg='Email Is Not Registered'
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'index.html')
	except:
		return render(request,'index.html')

