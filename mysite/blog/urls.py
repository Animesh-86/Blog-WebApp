from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),  
    path('add/', views.add_dataset_view, name='add_dataset'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('blog/<int:blog_id>/', views.view_blog, name='view_blog'),

]
