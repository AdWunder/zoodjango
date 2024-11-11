from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil 
    path('enclos/', views.liste_enclos, name='liste_enclos'),
    path('enclos/<int:enclos_id>/', views.detail_enclos, name='detail_enclos'),
    path('animal/<int:animal_id>/', views.detail_animal, name='detail_animal'),
    path('evenements/', views.liste_evenements, name='liste_evenements'),
    path('animaux/', views.liste_animaux, name='liste_animaux'),  
]
