"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from zoo import views  # Importer views de l'application zoo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zoo.urls')),  # Inclure les URLs de l'app 'zoo'
    
    # Routes pour les enclos et animaux
    path('', views.liste_enclos, name='liste_enclos'),
    path('enclos/<int:enclos_id>/', views.detail_enclos, name='detail_enclos'),
    path('animal/<int:animal_id>/', views.detail_animal, name='detail_animal'),
    
    # Routes pour les événements
    path('evenements/', views.liste_evenements, name='liste_evenements'),

    # Routes pour les soigneurs
    path('soigneurs/', views.liste_soigneurs, name='liste_soigneurs'),
    path('soigneur/<int:soigneur_id>/', views.detail_soigneur, name='detail_soigneur'),
]


