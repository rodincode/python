from django.urls import path
from . import views

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('login', views.loginview, name='login'),
    path('signup', views.signup, name='signup'),
    path('users', views.userview, name='users'),
    path('physim', views.physics_sim, name='physim'),
    path('chemsim', views.chemistry_sim, name='chemsim'),
    path('biosim', views.biology_sim, name='biosim'),
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    ]