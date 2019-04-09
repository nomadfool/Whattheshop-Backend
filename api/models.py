from django.db import models
from django.contrib.auth.models import User
# from phone_field import PhoneField

class Category(models.Model):
    name = models.CharField(max_length = 240)

    def __str__(self):
        return self.name



class Item(models.Model):
    name = models.CharField(max_length = 240)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10 , decimal_places = 2)
    image = models.ImageField(null =True , blank = True)
    category = models.ManyToManyField(Category)
    quantity = models.PositiveIntegerField()
    # inStock = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    # items = models.ManyToManyField(Item)
    user = models.ForeignKey(User , on_delete = models.CASCADE, null = True )
    status = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = 0
        for item in self.through.all():
            total += item.price
        return total


class ThroughCartItemModel(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE, related_name = 'through')
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()

class Address (models.Model):
    COUNTRIES = (
        ('Kuwait', 'Kuwait'),
        ('Oman','Oman'),
        ('UAE','UAE'),
        ('KSA','KSA'),
        ('Bahrain','Bahrain'),
        ('Qatar','Qatar'),
    )
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    country = models.CharField( choices = COUNTRIES , max_length = 20, default='Kuwait')
    city = models.CharField( max_length = 100, blank = True)
    state = models.CharField( max_length = 100, blank = True)
    zipcode = models.CharField(max_length = 5, blank = True)
    street_line1 = models.CharField( max_length = 100, blank = True)
    street_line2 = models.CharField( max_length = 100, blank = True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.PositiveIntegerField(blank=True, null = True)
    profile_image = models.ImageField(blank=True, null = True)
    # date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username
    # address = models.ForeignKey(Address ,null=True, on_delete = models.CASCADE)

   


   


