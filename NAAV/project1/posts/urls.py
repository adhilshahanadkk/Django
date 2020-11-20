from django.conf.urls import url
from django.urls import path
from posts import views as core_views
from posts.views import post_list, post_detail, new_post, contact, service, map1, map2, about

urlpatterns = [
    url('^$', post_list, name='post_list'),
    url(r'^contactus/$',contact ,name='contact'),
    path('posts/<int:pk>/',post_detail, name='post_detail'),
    path('posts/new/',new_post, name='post_new'),
    path('post/contactus',contact,name='contactus'),
    path('post/service',service,name='service'),
    path('post/map2',map2,name='map2'),
    path('post/map1',map1,name='map1'),
    path('post/about',about,name='about')
]