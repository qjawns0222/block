from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name='tesr'

urlpatterns= [
    path('',views.index,name='index'),
    path('trans/',views.trans,name='trans'),
    
    

]