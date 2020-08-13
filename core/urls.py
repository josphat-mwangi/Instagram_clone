from . import views
from django.conf.urls import url
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns=[
    # url(r'^$',views.home, name='home'),
    url(r'^$',views.userhome, name='userhome'),
    url(r'^search/', views.search, name='search'),
    url(r'^new_comment/(\d+)/$' ,views.add_comment,name='newComment'),
    url(r'^comment/(\d+)/$' ,views.comments,name='comments'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]