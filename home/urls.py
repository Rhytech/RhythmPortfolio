from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('websites',views.websites,name='websites'),
    path('articles',views.articles,name='articles'),
    path('designing',views.designing,name='designing'),
    path('contact',views.contact,name='contact'),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('signup',views.signup, name="signup")
]
