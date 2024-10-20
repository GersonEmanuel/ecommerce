from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'productst/list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

#def product_list_view(request):
#   queryset = Product.objects.all()
#   context = {'qs': queryset}
#   return render(request, products/jfj.html, context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'productst/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return super().get_object(queryset)
    
    #def get_object(self, *args, **kwargs):
        #pk = self.kwargs.get('pk')
        #instance = Product.objects.get_by_id(pk)
       # if instance is None:
         #   raise Http404("Esse produto não existe!")
        #return instance
    

#Function Based View
#def product_detail_view(request):
#   queryset = Product.objects.all()
#   context = {
#      'object_list': queryset
# }
#return render(request, "products/detail.html", context)