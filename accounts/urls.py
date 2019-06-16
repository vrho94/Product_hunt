from django.urls import path, include
from . import views#views.py znotraj aplikacije
urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
]
#login signup logout
