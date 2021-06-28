from django.shortcuts import render
from django.views import View
from home.models import product

class topwearList(View):

	sort="id"

	def get(self, request):
		cat = "topwear"
		prod = product.objects.filter(category=cat)[:20]
		for item in prod:
			item.image = 'products/'+item.image

		return render(request,'product_list.html',{"products":prod})

	def post(self, request):	

		if request.POST.get('prod_id'):
			prod_id = request.POST.get('prod_id')
			cart = request.session.get('cart')
			if not cart:
				cart = {}
				cart[prod_id] = 1
			else:
				if cart.get(prod_id):
					cart[prod_id] = cart.get(prod_id)+1
				else:
					cart[prod_id] = 1		

			request.session['cart'] = cart			


		if request.POST.get('sort'):
			self.sort=request.POST.get('sort')
		cat = "topwear"	
		prod = product.objects.filter(category=cat).order_by(self.sort)
		prod = list(prod)
		if self.sort in ["rating","arrival"]:
			prod.reverse()
		for item in prod:
			item.image = 'products/'+item.image

		return render(request,'product_list.html',{"products":prod[:20]})

class bottomwearList(View):

	def get(self, request):
		cat = "bottomwear"
		prod = product.objects.filter(category=cat)[:20]
		for item in prod:
			item.image = 'products/'+item.image

		return render(request,'product_list.html',{"products":prod})

	def post(self, request):	
		sort="id"
		if request.POST.get('sort'):
			sort=request.POST.get('sort')
		cat = "bottomwear"	
		prod = product.objects.filter(category=cat).order_by(sort)[:20]
		for item in prod:
			item.image = 'products/'+item.image

		return render(request,'product_list.html',{"products":prod})		

class accesoriesList(View):

	def get(self, request):
		cat = "accesories"
		prod = product.objects.filter(category=cat)[:20]
		for item in prod:
			item.image = 'products/'+item.image

		return render(request,'product_list.html',{"products":prod})

	def post(self, request):	
		sort="id"
		if request.POST.get('sort'):
			sort=request.POST.get('sort')
		cat = "accesories"	
		prod = product.objects.filter(category=cat).order_by(sort)[:20]
		for item in prod:
			item.image = 'products/'+item.image

		return render(request,'product_list.html',{"products":prod})