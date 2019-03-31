from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item ,Category ,ThroughCartItemModel , Cart


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many = True)
    class Meta:
        model = Item
        fields =  '__all__'

class CreateModelThrough(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField()
    class Meta:
        model = ThroughCartItemModel
        fields = ['id', 'item','quantity','cart'] 
        read_only_fields = ['cart']

    def get_cart(self, obj):
        return obj.cart.id





class CheckOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['status']       
        
# class ItemdetailSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(many = True)
#     class Meta:
#         model = Item
#         fields =  '__all__'