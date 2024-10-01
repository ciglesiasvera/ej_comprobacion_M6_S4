from django.contrib import admin
from django.urls import path, include
from book import views 

""" urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('book/', include('book.urls')),
] """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),  # Redirige la raíz a las URLs de book
]