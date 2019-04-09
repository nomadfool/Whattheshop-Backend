from rest_framework.generics import CreateAPIView, ListAPIView ,RetrieveUpdateAPIView ,RetrieveAPIView , DestroyAPIView
from .serializers import (UserCreateSerializer , ItemListSerializer ,UserCartHistory, CreateModelThrough , CheckOutSerializer, UserDataSerializer , ProfileSerializer , AddressSerializer, AddressCreateSerializer)
from .models import Item , Cart , Profile , Address,ThroughCartItemModel
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListAPIView(ListAPIView):
	queryset =  Item.objects.all()
	serializer_class = ItemListSerializer

class CreateModelThroughAPIView(CreateAPIView):
	
	serializer_class = CreateModelThrough


	def perform_create(self,serializer):
			cart_obj,create = Cart.objects.get_or_create(status = False , user = self.request.user )
			serializer.save(cart_id = cart_obj.id)

# class UpdateModelThroughAPIView(CreateAPIView):
# 	queryset = ThroughCartItemModel.objects.all()
# 	serializer_class = UpdateModelThrough
# 	lookup_field = 'id'
# 	lookup_url_kwarg = 'cart_id'
		


class CheckoutAPIView(APIView):
	def get(self, request):
		cart = Cart.objects.get(status=False, user=request.user)
		cart.status = True
		cart.save()
		return Response({"chechedOut":5})

class CartHistoryAPIView(ListAPIView):
	queryset = Cart.objects.all().order_by('-timestamp')
	serializer_class = UserCartHistory
	lookup_field = 'id'
	lookup_url_kwarg = 'cart_id'

class CartItemsHistoryAPIView(ListAPIView):
	serializer_class = CreateModelThrough

	def get_queryset(self):
		return ThroughCartItemModel.objects.filter(cart_id=self.kwargs['cart_id'])




	# def history(self, request, user_id):
	#  	user = User.objects.get(id = user_id)
	#  	cart = Cart.objects.filter(user = user)
	#  	response = {
	#  	'history':cart
	#  	}
	#  	return Response(response)

	

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