from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item ,Category ,ThroughCartItemModel , Cart ,Address, Profile



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password' , 'first_name' , 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']
        new_user = User(username=username, email=email , first_name = first_name, last_name = last_name)
        new_user.set_password(password)
        new_user.save()
        Profile.objects.create(user = new_user)
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


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    profile =  ProfileSerializer()
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ['id','username' , 'first_name' , 'last_name' , 'email' , 'profile', 'address'] 


                 