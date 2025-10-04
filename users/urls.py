from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test_view, name='test'),
    path('create/', views.create_product, name="create-product-view"),
    path('about/', views.about, name='about'),  # lista de productos
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),  # eliminar (POST)
]
