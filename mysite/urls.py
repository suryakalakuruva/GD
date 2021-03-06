"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', user_views.ProfileList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fb.urls')),
    path('register/', user_views.register, name='register' ),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('profile/', user_views.view_profile, name='profile'),
    path(r'^profile/(?P<pk>\d+)/$', user_views.view_profile, name='view_profile_with_pk'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    url(r'^password/$', user_views.change_password, name='change_password'),
    path('api/profile/', user_views.ProfileList.as_view()),
    path('api/profile/<int:pk>/', user_views.ProfileDetail.as_view()),
    # path('profiles/', user_views.ProfileList.as_view()),
    # path('profiles/<int:pk>/', user_views.ProfileDetail.as_view()),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)