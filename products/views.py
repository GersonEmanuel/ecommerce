from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

#def product_list_view(request):
#   queryset = Product.objects.all()
#   context = {'qs': queryset}
#   return render(request, products/jfj.html, context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    

#Function Based View
#def product_detail_view(request):
#   queryset = Product.objects.all()
#   context = {
#      'object_list': queryset
# }
#return render(request, "products/detail.html", context)