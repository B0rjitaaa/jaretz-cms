from django.shortcuts import render


def index(request):
	'''
	Main page of our app.
	The contents will be:
		- Banners.
		- Categories.
		- Items.
	'''
	return render(request, 'index.html', {})


def item(request, id_item):
	pass


def items(request):
	return render(request, 'item.html', {})


def category(request, id_category):
	pass


def categories(request):
	pass