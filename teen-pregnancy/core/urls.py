# core/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LoginView



urlpatterns = [
    
    path('', views.home, name='home'),
    path('forum/', views.forum, name='forum'),  # Forum list page
    path('resources/', views.resources, name='resources'),
    path('forum/<int:id>/', views.forum_detail, name='forum_detail'),  # URL pattern for forum_detail
    path('resource/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('forum/<int:post_id>/', views.forum_post_detail, name='forum_post_detail'),
    path('submit/resource/', views.submit_resource, name='submit_resource'),
    path('submit/forum/', views.submit_forum_post, name='submit_forum_post'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
