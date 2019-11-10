from rest_framework.serializers import ModelSerializer
from .models import Product, Book

class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ('product_name', 
		'product_price'
		'product_avaliable_count',
		'product_detail',
		'product_can_be_sold',
		'product_created_updated')
class BookSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = ('author_name',
		'gengre',
		'publishing_house',
		'Publication_date', 
		'Number_of_pages'
		)
