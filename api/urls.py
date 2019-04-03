from django.urls import path
from .views import UserCreateAPIView ,ItemListAPIView , CreateModelThroughAPIView , CheckoutAPIView , EditProfileAPIView ,UserDataAPIView, CreateAddressAPIView, EditAddressAPIView, DestroyAddressAPIView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ItemListAPIView.as_view(), name = 'list'),
    path('cart/', CreateModelThroughAPIView.as_view(), name ='cart'),
    path('checkout/<int:cart_id>/' , CheckoutAPIView.as_view() , name ='checkout'),
    path('profile/<int:profile_id>/edit/',EditProfileAPIView.as_view(), name = 'edit-profile' ),
    path('user/<int:user_id>/data/',UserDataAPIView.as_view(), name = 'user-profile' ),
    path('address/create/',CreateAddressAPIView.as_view(), name = 'address-create' ),
    path('address/<int:address_id>/edit/',EditAddressAPIView.as_view(), name = 'address-edit' ),
    path('address/<int:address_id>/delete/',DestroyAddressAPIView.as_view(), name = 'address-delete' ),
    # path('detail/<int:item_id>/', ItemDetailAPIView.as_view(), name = 'detail'),
]