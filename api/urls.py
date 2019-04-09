from django.urls import path
from .views import UserCreateAPIView ,ItemListAPIView , CreateModelThroughAPIView , CheckoutAPIView , EditProfileAPIView ,UserDataAPIView, CreateAddressAPIView, EditAddressAPIView, DestroyAddressAPIView, CartHistoryAPIView,CartItemsHistoryAPIView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ItemListAPIView.as_view(), name = 'list'),
    path('cart/', CreateModelThroughAPIView.as_view(), name ='cart'),
    # path('cart/<int:cart_id>/update/',UpdateModelThroughAPIView.as_view(), name='update-cart'),
    path('cart/<int:cart_id>/', CartItemsHistoryAPIView.as_view(), name ='cart-Item'),
    path('checkout/' , CheckoutAPIView.as_view() , name ='checkout'),
    path('profile/<int:profile_id>/edit/',EditProfileAPIView.as_view(), name = 'edit-profile' ),
    path('user/<int:user_id>/data/',UserDataAPIView.as_view(), name = 'user-profile' ),
    path('address/create/',CreateAddressAPIView.as_view(), name = 'address-create' ),
    path('address/<int:address_id>/edit/',EditAddressAPIView.as_view(), name = 'address-edit' ),
    path('address/<int:address_id>/delete/',DestroyAddressAPIView.as_view(), name = 'address-delete' ),
    path('history/', CartHistoryAPIView.as_view(), name = 'history'),
]