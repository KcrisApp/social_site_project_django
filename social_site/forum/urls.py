from django.urls import path
from . import views

urlpatterns = [
 
    path('nuova-sezione/', views.CreaSezione.as_view() , name='crea_sezione'),
    path('sezione/<int:pk>/', views.visualizza_sezione , name='sezione_view'),
    path('sezione/<int:pk>/crea-discussione', views.crea_discussione , name='crea_discussione'),
    # path('user/<str:username>/', views.user_profile_view , name='user_profile'),
    
]