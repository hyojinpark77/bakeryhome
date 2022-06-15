from homepage import views
from django.urls import path
#TEMPLATE TAGGING
app_name = 'homepage'

urlpatterns= [
    path('homepage/login', views.login,name='login'),
    path('homepage/join', views.join,name='join'),
    path('homepage/new_product', views.new_product,name='new_product'),
]