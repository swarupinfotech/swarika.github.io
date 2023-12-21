from django.db import models

# Create your models here.
class Book_Table(models.Model):
    Name = models.CharField(max_length=55)
    Email = models.EmailField(max_length=55)
    Number = models.IntegerField()
    Date = models.DateField()
    Person = models.IntegerField() 

class Employees(models.Model):
    First_Name = models.CharField(max_length=55)
    Last_Name = models.CharField(max_length=55)
    Email = models.EmailField(max_length=55)
    Username = models.CharField(max_length=55)
    Password = models.CharField(max_length=55)
    Coins = models.IntegerField(default=100)

class Items(models.Model):
    Title = models.CharField(max_length=55)
    Type = models.CharField(max_length=10, default='')
    Decription = models.TextField(max_length=250)
    Price = models.IntegerField()
    Quantity = models.IntegerField(default=0)
    Image = models.FileField(upload_to='items_image/', max_length=250, null=True, default=None)

    def save(self, *args, **kwargs):
        # Convert the 'type' field to lowercase before saving
        self.Type = self.Type.lower()
        super(Items, self).save(*args, **kwargs)

class CardItems(models.Model):
    Username = models.CharField(max_length=50, default="")
    Image = models.CharField(max_length=100)
    Name = models.CharField(max_length=55)
    Type = models.CharField(max_length=10)
    Price = models.IntegerField()
    UserId = models.IntegerField()
    Quantity = models.IntegerField(default=1)

class ItemsOrder(models.Model):
    Image = models.CharField(max_length=100)
    Name = models.CharField(max_length=55)
    Type = models.CharField(max_length=10)
    Price = models.IntegerField()
    Username = models.CharField(max_length=50, default="")
    Quantity = models.IntegerField()