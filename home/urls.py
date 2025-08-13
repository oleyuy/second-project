from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('register/', views.register_view, name='register'),
    path('login/',views.login_view(template_name='account/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]