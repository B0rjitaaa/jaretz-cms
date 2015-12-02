from django.shortcuts import render

from shop.models import Item, Banner, Shop, Offer, Category

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
	banners = Banner.objects.all()

	response = {
		'categories': Category.objects.all().filter(parent_category=None),
		'recent_items': recent_items,
		'featured_items': featured_items,
		'popular_items': popular_items,
		'banners': banners,
		'offers': Offer.objects.all()[:2],
		'shop_info': Shop.objects.all()[0]

	}
	return render(request, 'index.html', response)


def item(request, item_slug, item_id):
	item = Item.objects.get(pk=item_id)
	response = {
		'shop_info': Shop.objects.all()[0],
		'item': item,
		'items': item.category.items.all().exclude(reference_code=item.reference_code)
	}
	return render (request, 'item.html', response)


def items(request):
	response = {
		'shop_info': Shop.objects.all()[0],
		'categories': Category.objects.all().filter(parent_category=None)
	}
	return render(request, 'product.html', response)


def category(request, category_slug, category_id):
	response = {
		'shop_info': Shop.objects.all()[0],
		'category': Category.objects.get(pk=category_id)
	}
	return render(request, 'category.html', response)


def categories(request):
	response = {
		'shop_info': Shop.objects.all()[0],
		'categories': Category.objects.all().filter(parent_category=None)
	}
	return render(request, 'categories.html', response)


def contact(request):
	response = {
		'shop_info': Shop.objects.all()[0],
		'categories': Category.objects.all().filter(parent_category=None)
	}
	return render (request, 'contact.html', response)