from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView),
    path('logout/', auth_views.LogoutView),

]
