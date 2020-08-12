from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^comment/(\d+)$', views.comment, name="comment"),
    url(r'^post/$', views.posts,name='uploadpost'),
]