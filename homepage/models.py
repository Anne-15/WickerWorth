from django.db import models

# Create your models here.

class PersonInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField
    phone_number = models.IntegerField

    def __str__(self):
        return self.first_name

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    phone_number = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search

