from django.urls import path
app_name = 'search'

from .views import *

urlpatterns = [
    path('', SearchProductView.as_view(), name='query')
]
