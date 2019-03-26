from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer , ItemListSerializer
from .models import Item

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListAPIView(ListAPIView):
	queryset =  Item.objects.all()
	serializer_class = ItemListSerializer
