from django.contrib import admin
from .models import Item , Category ,Cart , ThroughCartItemModel

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(ThroughCartItemModel)