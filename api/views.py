from rest_framework.generics import CreateAPIView, ListAPIView ,RetrieveUpdateAPIView ,RetrieveAPIView , DestroyAPIView
from .serializers import (UserCreateSerializer , ItemListSerializer , CreateModelThrough , CheckOutSerializer, UserDataSerializer , ProfileSerializer , AddressSerializer, AddressCreateSerializer)
from .models import Item , Cart , Profile , Address
from django.contrib.auth.models import User

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

class EditProfileAPIView(RetrieveUpdateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'profile_id'

class CreateAddressAPIView(CreateAPIView):
	serializer_class = AddressCreateSerializer
	

class EditAddressAPIView(RetrieveUpdateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'

class DestroyAddressAPIView(DestroyAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'	

class UserDataAPIView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserDataSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'user_id'