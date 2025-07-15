# gallery/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Auth routes
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # User profile
    path('profile/', views.profile_view, name='profile'),

    # Home page
    path('', views.home_view, name='home'),

    # Photo upload
    path('upload/', views.upload_photo_view, name='upload'),

    # Gallery view
    path('photos/', views.photo_list_view, name='photo_list'),
]
