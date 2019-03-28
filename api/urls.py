from django.urls import path
from .views import UserCreateAPIView ,ItemListAPIView , CreateModelThroughAPIView , CheckoutAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ItemListAPIView.as_view(), name = 'list'),
    path('cart/', CreateModelThroughAPIView.as_view(), name ='cart'),
    path('checkout/<int:cart_id>/' , CheckoutAPIView.as_view() , name ='checkout')
    # path('detail/<int:item_id>/', ItemDetailAPIView.as_view(), name = 'detail')
]