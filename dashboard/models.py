from django.db import models

class Category(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=50, unique=True)

class Product(models.Model):
  id = models.BigAutoField(primary_key=True)
  title = models.CharField(max_length=264)
  sub_title = models.CharField(max_length=264)
  details = models.TextField()
  price = models.DecimalField(decimal_places=2,max_digits=10)
  price_discount = models.DecimalField(decimal_places=2,max_digits=10)
  material_care = models.TextField()
  reviews = models.IntegerField()

class PropertyProductImage(models.Model):
  id = models.BigAutoField(primary_key=True)
  product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
  image = models.ImageField()

class PropertyProductBlog(models.Model):
  id = models.BigAutoField(primary_key=True)
  product = models.ForeignKey(Product, related_name='blogs', on_delete=models.CASCADE)
  title = models.CharField(max_length=264)
  sub_title = models.CharField(max_length=264)
  image = models.ImageField(upload_to='upload')