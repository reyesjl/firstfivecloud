from django.urls import path
from . import views

urlpatterns = [
  path('', views.handleFetchProducts, name='catalog'),
  path('add_product/', views.handleAddProduct, name='add_product')
]

