from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    
    def get_queryset(self, *args, **kargs):
        request = self.request
        result = request.GET
        print('Resultado:', result)
        query = result.get('q', None) # result['q']
        print('Consulta', query)
        if query is not None:
            return Product.objects.filter(title__iexact = query)
        return Product.objects.featured()
