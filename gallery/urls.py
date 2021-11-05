from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name='gallery'

urlpatterns= [
    path('',views.index,name='index'),
    path('detail/<dpk>',views.detail,name='detail'),
    path('create/',views.create,name='create'),
    path('chdel/<dpk>',views.chdel,name='chdel'),
    path('mod/<dpk>',views.mod,name='mod'),
    path('delrep/<gpk>/<dpk>',views.delrep,name='delrep'),
    path('createreply/<dpk>',views.createreply,name='createreply'),
]