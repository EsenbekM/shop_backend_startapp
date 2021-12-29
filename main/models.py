from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 



class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    imege = models.ImageField(upload_to='')
    description = models.TextField()
    price = models.FloatField() 
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 