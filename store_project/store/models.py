from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    price = models.IntegerField()
    categories = models.ManyToManyField('Category', blank=True, related_name='products')
    image = models.ImageField(upload_to='images/', default='images/default.webp')

    def __str__(self) -> str:
        return self. title

class Category(models.Model):
   title = models.CharField(max_length=150)

   def __str__(self) -> str:
        return self. title

   class Meta:
    verbose_name_plural = "Categories"

class Order(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.user_name