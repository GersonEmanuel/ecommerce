from django.db import models

#Custom Queryset
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)
    
    def featured(self):
        return self.filter(active = True, featured = True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active
    
    def featured(self):
        return self.get_queryset().featured()
    

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() ==1:
            return qs.first()
        return None
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank = True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits = 20, default=10)
    image = models.ImageField(upload_to= 'products/', null=True, blank=True)
    objects = ProductManager()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default = True)
 
    def __str__(self):
        return self.title
    
