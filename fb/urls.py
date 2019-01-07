from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('post_list/',views.post_list,name='post_list'),
    path('create_post/',views.create_post,name='create_post'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/comment/',views.create_comment,name='create_comment'),
    path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
]