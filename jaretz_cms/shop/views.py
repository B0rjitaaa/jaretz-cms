from django.shortcuts import render


def index(request):
	'''
	Main page of our app.
	The contents will be:
		- Banners.
		- Categories.
		- Items.
	'''
	return render(request, 'base.html', {})


def item(request, id_item):
	pass


def items(request):
	pass


def category(request, id_category):
	pass


def categories(request):
	pass