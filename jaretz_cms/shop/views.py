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
	recent_items = Item.objects.order_by('-upload_date')[:12]
	featured_items = Item.objects.filter(starred=True)[:12]
	popular_items = Item.objects.order_by('shown_times')[:12]

	response = {
		'recent_items': recent_items,
		'featured_items': featured_items,
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