from django.db import models
from .utils import token_hex

# Create your models here.

class WarehouseProduct(models.Model):

	class Meta:
		verbose_name = 'product'
		verbose_name_plural = 'products'

	PRODUCTTYPECHOICES = (
		("banana", "Banana"),
		("apple", "Apple"),
		("orange", "Orange")
	)
	
	title = models.CharField(
		max_length=255,
		db_index=True,
		null=True,
		default=None,
		blank=True
	)

	_article = models.CharField(
		max_length=255,
		db_index=True,
		null=True,
		default=None,
		blank=True
	)

	_type = models.CharField(
		max_length=255,
		null=True,
		default=None,
		blank=True,
		choices=PRODUCTTYPECHOICES
	) 

	description = models.TextField(default=None, null=True, blank=True)
	price = models.FloatField(default=None, null=True, blank=True)


	in_stock = models.BooleanField(default=True)


	def __str__(self):
		return str(self.id)


	def check_stock(self):
		if self.in_stock:
			return True
		else:
			return False

	def gen_unique_article():
		last = WarehouseProduct.objects.all().last()
		return f"{int(last.id) + 1}-{token_hex(2)}/{token_hex(3)}".upper()

	def check_article(func):
		def wrapper(obj, *args, **kwargs):
			if not obj._article:
				obj._article = WarehouseProduct.gen_unique_article()
				super(WarehouseProduct, obj).save(*args, **kwargs)
				return func(obj, *args, **kwargs)
		return wrapper

	#@check_article
	def save(self, *args, **kwargs):
		return super(WarehouseProduct, self).save(*args, **kwargs)