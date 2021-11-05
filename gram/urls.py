from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name='gram'

urlpatterns= [
    path('<un>',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('search/<name>',views.search,name='search'),
]