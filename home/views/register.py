from django.shortcuts import render,redirect
from django.views import View
from home.models import customer
import datetime

class Register(View):

	def get(self ,request):

		return render(request,'register.html')

	def post(self, request):
		
		message = list()
		if not request.POST.get("name"):
			message.append("Name cannot be left empty")

		if not request.POST.get("mobile"):
			message.append("Phone no. cannot be left empty")
		else:
			for item in request.POST.get("mobile"):
				if not item.isdigit():
					message.append("Wrong phone number")
					break

		if not request.POST.get("email"):
			message.append("Email cannot be left empty")

		if not request.POST.get("password"):
			message.append("Password cannot be left empty")
		else:	
			if len(request.POST.get("password"))<6:
				message.append("Password should be more than 6 characters")	

		if message:		
		
			return render(request,'register.html',{"msg":message,"data":request.POST})			
		else:
			name = request.POST.get("name")
			phone = request.POST.get("mobile")
			email = request.POST.get("email")
			password = request.POST.get("password")
			join_data = datetime.date.today()
			cus = customer(name=name,phone=phone,email=email,password=password,join_data=join_data).save()
			return redirect("/login")	


class Login(View):

	def get(self, request):

		return render(request, 'login.html')		

	def post(self, request):
		
		message = list()

		if not request.POST.get("email"):
			message.append("Email cannot be left empty")

		if not request.POST.get("password"):
			message.append("Password cannot be left empty")

		if message:		
		
			return render(request,'login.html',{"msg":message,"data":request.POST})			
		else:
			try:
				user = customer.objects.get(email=request.POST['email'])
			except:
				user = None

			if user:
				if user.password==request.POST['password']:
					request.session['user'] = request.POST['email']
					return redirect("/home")
				else:
					message.append("Wrong username or password")
					return render(request,'login.html',{"msg":message,"data":request.POST})			
			else:
				message.append("Username does not exists")
				return render(request,'login.html',{"msg":message,"data":request.POST})		

class Logout(View):
	
	def get(self, request):

		request.session.flush()
		return redirect("/home")
										