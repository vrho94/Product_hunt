from django.urls import path, include
from . import views#views.py znotraj aplikacije
urlpatterns = [
    path('create', views.create_product, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),  
]
