from django.contrib import admin
from .models import *
from .forms import *


class StockCreateAdmin(admin.ModelAdmin):
	list_display = ['category', 'item_name', 'quantity']  #display fields in tabular format
	form = StockCreateForm  # show only specifield fields of form
	list_filter = ['category'] # Side filters
	search_fields  = ['category', 'item_name'] #search option

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
