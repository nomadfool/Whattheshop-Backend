from rest_framework.generics import CreateAPIView, ListAPIView ,RetrieveUpdateAPIView
from .serializers import (UserCreateSerializer , ItemListSerializer , CreateModelThrough , CheckOutSerializer)
from .models import Item , Cart

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListAPIView(ListAPIView):
	queryset =  Item.objects.all()
	serializer_class = ItemListSerializer

class CreateModelThroughAPIView(CreateAPIView):
	
	serializer_class = CreateModelThrough


	def perform_create(self,serializer):
			cart_obj,create = Cart.objects.get_or_create(status = False , user = self.request.user )

			serializer.save(cart = cart_obj)


class CheckoutAPIView(RetrieveUpdateAPIView):
	queryset = Cart.objects.all()
	serializer_class = CheckOutSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'cart_id'
# class ItemDetailAPIView(ListAPIView):
# 	 queryset = Item.objects.all()
# 	 serializer_class = ItemdetailSerializer
# 	 lookup_field = 'id'
# 	 lookup_url_kwarg = 'item_id'