from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^new_comment/(\d+)/$' ,views.add_comment,name='newComment'),
    url(r'^comment/(\d+)/$' ,views.comments,name='comments'),
    url(r'^post/$', views.posts,name='uploadpost'),
]