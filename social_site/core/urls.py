from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view() , name='homepage'),
    path('users/', views.UserListView.as_view() , name='users_list'),
    path('cerca/', views.cerca , name='funzione_cerca'),
    path('user/<str:username>/', views.user_profile_view , name='user_profile'),
    
]