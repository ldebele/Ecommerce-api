from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class Book(models.Model):
    title = models.EmailField(max_length=255)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=15)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['date_created']


    def __str__(self):
        return self.title



class Product(models.Model):
    product_tag = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
     