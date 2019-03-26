from django.db import models

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


