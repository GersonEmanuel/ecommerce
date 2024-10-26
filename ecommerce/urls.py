from django.conf import settings
from django.urls import path
from products.views import *
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path("aboutpage/", about_page, name='about'),
    path('contactpage/', contact_page, name= 'contact' ),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('featured/', ProductFeaturedListView.as_view(), name = 'featuredlistview'),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view(), name='featureddetailview'),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view(), name= 'detailslug')
]


