from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name
  
class News(models.Model):
  title = models.CharField(max_length=100)
  short_description = models.TextField(max_length=400)
  long_description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='noticias_images/', null=True, blank=True)
  
  def __str__(self):
    return self.title
  