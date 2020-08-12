from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.home, name='home'),
    url(r'^search/', views.search, name='search')
]