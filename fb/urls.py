from django.urls import path,include
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')



urlpatterns = [
    path('', views.start, name='start'),
    path('post_list/',views.post_list,name='post_list'),
    path('create_post/',views.create_post,name='create_post'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/comment/',views.create_comment,name='create_comment'),
    path('search/',views.search,name='search'),
    path('friends/',views.friends_list,name='friends_list'),
    path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    path('likes/',views.like_post, name='like_post'),

    path('api/', views.PostList.as_view()),
    path('api/<int:pk>/', views.PostDetail.as_view()),
    path('api/comment/', views.CommentList.as_view()),
    path('api/comment/<int:pk>/', views.CommentDetail.as_view()),
    # path('post/', views.PostList.as_view()),
    # path('post/<int:pk>/', views.PostDetail.as_view()),
    # path('comment/', views.CommentList.as_view()),
    # path('comment/<int:pk>/', views.CommentDetail.as_view()),
  
    path('list/', schema_view)

]