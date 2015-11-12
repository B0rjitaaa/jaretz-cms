from django.shortcuts import render

from shop.models import Item

def index(request):
	'''
	Main page of our app.
	The contents will be:
		- Banners.
		- Categories.
		- Items.
	'''
	popular_items = Item.objects.order_by('shown_times')
	response = {
		'popular_items': popular_items
	}
	return render(request, 'index.html', response)


def item(request, id_item):
	pass


def items(request):
	return render(request, 'item.html', {})


def category(request, id_category):
	pass


def categories(request):
	pass