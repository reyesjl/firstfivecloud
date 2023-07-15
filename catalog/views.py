from django.shortcuts import render
from .models import Product, Category

def handleFetchProducts(request):
	'''
		Returns all products from the catalog that are active by default
	'''
	categories = Category.objects.all()
	products = Product.objects.filter(is_active=True)
	return render(request, 'products/product_list.html', {'products':products, 'categories':categories})
