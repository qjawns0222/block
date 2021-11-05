from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name='vote'

urlpatterns= [
    path('',views.index,name='index'),
    path('detail/<dpk>',views.detail,name='detail'),
    path('vote/<tpk>',views.vote,name='vote'),
    path('cancel/<cpk>',views.cancel,name='cancel'),
    path('create/',views.create,name='create'),
    path('delrep/<dpk>/<tpk>',views.delrep,name='delrep'),
    path('createreply/<dpk>',views.createreply,name='createreply'),

]