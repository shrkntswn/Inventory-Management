from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=50, blank=False, null=True)
	def __str__(self):
		return self.name

class Stock(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	item_name = models.CharField(max_length=50, blank=False, null=True)
	quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
	receive_quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.PositiveIntegerField(default=0, blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now = True)
	export_to_csv = models.BooleanField(default=False)

	def __str__(self):
		return self.item_name + " " + str(self.quantity)