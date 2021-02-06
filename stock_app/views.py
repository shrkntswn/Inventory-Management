from django.shortcuts import render, redirect
from .models import Stock
from .forms import *


def home(request):
	homeActive=True
	title = "Home"
	context = {'title':title,'homeActive':homeActive}
	return render(request, 'stock/home.html', context)

def list_item(request):
	list_itemActive =True
	title = "Items list"
	stocks = Stock.objects.all()
	#search_by_category = request.GET.get('search1')
	search_by_item_name = request.GET.get('search2')
	form = StockSearchForm(request.GET)
	if search_by_item_name:
		stocks = Stock.objects.filter(item_name__icontains=search_by_item_name)
		context = {'form':form, 'stocks':stocks, 'list_itemActive':list_itemActive}
	context = {'form':form,'title':title, 'stocks':stocks, 'list_itemActive':list_itemActive}
	return render(request, 'stock/list_item.html', context)

def add_item(request):
	add_itemActive=True
	title = "Add item"
	form = StockCreateForm()
	if request.method == 'POST':
		form = StockCreateForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('add_item')
	context = {'title':title,'form':form, 'add_itemActive':add_itemActive}
	return render(request, 'stock/add_item.html', context)

def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('list_item')
	context = {'form':form}
	return render(request, 'stock/add_item.html', context)

def delete_item(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
	return redirect('list_item')
