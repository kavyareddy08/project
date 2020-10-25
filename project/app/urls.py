from django.contrib import admin
from django.urls import path,include 
from app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('handleBlog',views.handleBlog,name='handleBlog'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('addnote',views.addnote,name='addnote'),
    path('search',views.search,name='search'),
    path('signin',views.signin,name='signin'),
    
]