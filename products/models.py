from django.db import models
from django.db.models import Q
from ecommerce.utils import unique_order_id_generator
from django.db.models.signals import pre_save
from django.urls import reverse

#Custom Queryset
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)
    
    def featured(self):
        return self.filter(active = True, featured = True)
    
    def search(self, query):
        lookups = (Q(title__contains = query) | Q(description__contains = query)| Q(price__contains = query)| Q(tag__title__icontains=query))
        return self.filter(lookups).distinct()
    

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured()
    

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() ==1:
            return qs.first()
        return None
    
    def search(self, query):
        return self.get_queryset().active().search(query)
    
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank = True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits = 20, default=10)
    image = models.ImageField(upload_to= 'products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()
    
 
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug = self.slug)
        return reverse('products:detail', kwargs={'slug':self.slug})
    
    
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_order_id_generator(instance)

pre_save.connect(product_pre_save_receiver, sender= Product)
    
