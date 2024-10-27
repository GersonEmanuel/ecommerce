from django.urls import path

app_name = 'carts'

from .views import *

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update' )
]
