from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path("aboutpage/", about_page, name='about'),
    path('contactpage/', contact_page, name= 'contact' ),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA.ROOT)
