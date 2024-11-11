from django.shortcuts import render, get_object_or_404, redirect
from .models import Enclos, Animal, Evenement, Soigneur
from .forms import ChangeEnclosForm

def index(request):
    enclos_list = Enclos.objects.all()
    animaux_list = Animal.objects.all()
    soigneurs_list = Soigneur.objects.all()
    evenements_list = Evenement.objects.all()
    
    context = {
        'enclos_list': enclos_list,
        'animaux_list': animaux_list,
        'soigneurs_list': soigneurs_list,
        'evenements_list': evenements_list,
    }
    return render(request, 'zoo/index.html', context)


def liste_enclos(request):
    enclos = Enclos.objects.all()
    return render(request, 'zoo/liste_enclos.html', {'enclos': enclos})

def detail_enclos(request, enclos_id):
    enclos = Enclos.objects.get(id=enclos_id)
    return render(request, 'zoo/detail_enclos.html', {'enclos': enclos})

def detail_animal(request, animal_id):
    # Récupère l'animal avec l'ID spécifié
    animal = get_object_or_404(Animal, id=animal_id)
    
    if request.method == 'POST':
        form = ChangeEnclosForm(request.POST, instance=animal)
        if form.is_valid():
            form.save() 
            return redirect('detail_animal', animal_id=animal.id)  
    else:
        form = ChangeEnclosForm(instance=animal) 

    context = {
        'animal': animal,
        'form': form,
    }
    
    return render(request, 'zoo/detail_animal.html', context)

def liste_animaux(request):
    animaux = Animal.objects.all() 
    return render(request, 'zoo/liste_animaux.html', {'animaux': animaux})

def liste_evenements(request):
    evenements = Evenement.objects.all()
    return render(request, 'zoo/liste_evenements.html', {'evenements': evenements})

def liste_soigneurs(request):
    soigneurs = Soigneur.objects.all()
    return render(request, 'zoo/liste_soigneurs.html', {'soigneurs': soigneurs})

def detail_soigneur(request, soigneur_id):
    soigneur = get_object_or_404(Soigneur, pk=soigneur_id)
    return render(request, 'zoo/detail_soigneur.html', {'soigneur': soigneur})
