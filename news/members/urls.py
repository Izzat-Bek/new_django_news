from django.urls import path
from .views import register_view, login_view, logout_request
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_view, name='register' ),
    path('login', login_view, name='login' ),
    path('logout', logout_request, name='logout' ),

]

    