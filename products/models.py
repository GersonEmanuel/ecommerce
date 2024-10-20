from django.db import models

class ProductManager(models.Manager):
    def active(self):
        return self.filter(active = True)
    
    def featured(self):
        return self.filter(active = True, featured = True)
    
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() ==1:
            return qs.first()
        return None
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits = 20, default=10)
    image = models.ImageField(upload_to= 'products/', null=True, blank=True)
    objects = ProductManager()
 
    def __str__(self):
        return self.title
    
