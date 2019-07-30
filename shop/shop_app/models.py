from django.db import models
from django.contrib.auth.models import User
from warehouse_app.models import WarehouseProduct

from API.rest_framework.api_utils import check_stock

# Create your models here.

class Personal(User):
	class Meta:
		verbose_name = 'personal'
		verbose_name_plural = 'personal'

	is_shop_manager = models.BooleanField(default=False)
	is_warehouse_manager = models.BooleanField(default=False)


class Promotion(models.Model):
	class Meta:
		verbose_name = 'promotion'
		verbose_name_plural = 'promotions'

	title = models.CharField(
		max_length=255,
		db_index=True,
		null=True,
		default=None,
		blank=True
	)

	amount = models.PositiveIntegerField(
		default=None,
		null=True,
		blank=True,
		verbose_name='promotion %'
	)

	def __str__(self):
		return str(self.id)

class ShopProduct(WarehouseProduct):

	'''
	Warehouse fields:
		title = CharField
		_article = CharFiel
		_type = CharField
		description TextField
		price = FloatField
		in_stock = BooleanField
	'''

	class Meta:
		verbose_name = 'product'
		verbose_name_plural = 'products'

	promotions = models.ManyToManyField(
		'shop_app.Promotion',
		default=None,
		blank=True,
		verbose_name='Акции'
	)

	def __str__(self):
		return str(self.id)

	def update_stock(func):
		def wrapper(self, *args, **kwargs):
			if check_stock:
				self.in_stock = True
				super(ShopProduct, self).save(*args, **kwargs)
				return func(self, *args, **kwargs)
			else:
				self.in_stock = False
				super(ShopProduct, self).save(*args, **kwargs)
				return func(self, *args, **kwargs)

		return wrapper

	@update_stock
	def save(self, *args, **kwargs):
		return super(ShopProduct, self).save(*args, **kwargs)


class Order(models.Model):
	class Meta:
		verbose_name = 'order'
		verbose_name_plural = 'orders'

	title = models.CharField(
		max_length=255,
		db_index=True,
		null=True,
		default=None,
		blank=True
	)

	basket = models.ManyToManyField(
		'shop_app.ShopProduct',
		default=None,
		blank=True,
		verbose_name='Корзина'
	)

	full_price = models.FloatField(
		default=None,
		null=True,
		blank=True,
		verbose_name='Итоговая стоимость'
	)

	customer = models.ForeignKey(User, on_delete="CASCADE")

	is_active = models.BooleanField(default=True)
	is_valid = models.BooleanField(default=False)
	is_canceled = models.BooleanField(default=False)
	is_stoped = models.BooleanField(default=False)
	is_payed = models.BooleanField(default=False)
	is_delivered = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)



	# def save(self, *args, **kwargs):
	# 	return super(Order, self).save(*args, **kwargs)