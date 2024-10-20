from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from products.views import ProductListView, ProductDetailView
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path("aboutpage/", about_page, name='about'),
    path('contactpage/', contact_page, name= 'contact' ),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('products', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
