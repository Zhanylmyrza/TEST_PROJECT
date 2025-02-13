from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    buyers = models.ManyToManyField(User, related_name="bought_products")  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    bio = models.TextField()
