from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()

#def product_list_view(request):
#   queryset = Product.objects.all()
#   context = {'qs': queryset}
#   return render(request, products/jfj.html, context)
