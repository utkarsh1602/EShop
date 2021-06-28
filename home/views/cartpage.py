from django.shortcuts import render,redirect
from django.views import View
from home.models import product

class Cart(View):

	def get(self, request):

		items = list()
		total_cart_value = 0
		if request.session.get('cart'):
			ids = request.session.get('cart').keys()
			prod = product.objects.filter(id__in=ids)
			for i in prod:
				a={}
				a['image'] = 'products/'+i.image
				a['name'] = i.name
				a['brand'] = i.brand
				a['price'] = i.selling_price
				a['id'] = i.id
				total_cart_value += int(i.selling_price)*(request.session.get('cart').get(str(i.id)))
				items.append(a)

			request.session['total_cart_value'] = total_cart_value	

		return render(request,"cart.html",{'items':items,'total_cart_value':total_cart_value})

	def post(self, request):

		items = list()
		total_cart_value = 0
		if request.session.get('cart'):

			if request.POST.get("edit"):
				cart = request.session.get('cart')
				edit = request.POST.get('edit')
				prod_id = request.POST.get('product_id')

				if edit=='inc':
					cart[prod_id] += 1
				if edit=='dec':
					cart[prod_id] -= 1	
					if cart[prod_id]<1:
						del cart[prod_id]

				request.session['cart'] = cart	

			ids = request.session.get('cart').keys()
			prod = product.objects.filter(id__in=ids)
			for i in prod:
				a={}
				a['image'] = 'products/'+i.image
				a['name'] = i.name
				a['brand'] = i.brand
				a['price'] = i.selling_price
				a['id'] = i.id
				total_cart_value += int(i.selling_price)*(request.session.get('cart').get(str(i.id)))
				items.append(a)

			request.session['total_cart_value'] = total_cart_value	

		return render(request,"cart.html",{'items':items,'total_cart_value':total_cart_value})