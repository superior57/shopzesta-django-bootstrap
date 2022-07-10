from unicodedata import category
from django.db import models

class Category(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return str(self.name)

class Brand(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return str(self.name)

class Product(models.Model):
  GENDERS = (
    ('men', 'Men'),
    ('women', 'Women'),
  )
  SIZES = (
    ('s', 'S (27)'),
    ('m', 'M (18)'),
    ('l', 'L (0)'),
    ('xl', 'XL (1)'),
    ('xxl', 'XXL (2)'),
  )

  id = models.BigAutoField(primary_key=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
  gender = models.CharField(max_length=6, choices=GENDERS, default='men')
  size = models.CharField(max_length=6, choices=SIZES, default='m')
  title = models.CharField(max_length=264)
  sub_title = models.CharField(max_length=264)
  details = models.TextField()
  price = models.DecimalField(decimal_places=2,max_digits=10)
  price_discount = models.DecimalField(decimal_places=2,max_digits=10)
  material_care = models.TextField()
  reviews = models.IntegerField(default=0)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

class PropertyProductImage(models.Model):
  id = models.BigAutoField(primary_key=True)
  product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
  image = models.ImageField(upload_to='products')

class PropertyProductBlog(models.Model):
  id = models.BigAutoField(primary_key=True)
  product = models.ForeignKey(Product, related_name='blogs', on_delete=models.CASCADE)
  title = models.CharField(max_length=264)
  sub_title = models.CharField(max_length=264)
  image = models.ImageField(upload_to='products')