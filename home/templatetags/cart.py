from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product, cart):

	keys = cart.keys()
	for item in keys:
		if str(product)==str(item):
			return True 
	return False

@register.filter(name="quantity")
def quantity(product, cart):	

	quantity = cart.get(str(product))
	
	return quantity 

@register.filter(name="total")
def total_quant(cart):
	total = 0
	if cart:
		for item in cart.keys():
			total += cart.get(item)
	return total

@register.filter(times="range")
def times(num):
	return range(num)	

@register.filter(name="total_cost")
def total_cost(quantity, price):
	
	return int(quantity)*int(price)

@register.filter(name="sum")
def sum(num1,num2):
	return num1+num2	