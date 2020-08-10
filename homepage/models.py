from django.db import models

# Create your models here.

class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField
    phone_number = models.IntegerField

    def __str__(self):
        return self.first_name

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=1000)
    phone_number = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search

