import json
from datetime import datetime
from django.core.management.base import BaseCommand
from zoo.models import Enclos, Animal, Soigneur, Evenement

class Command(BaseCommand):
    help = 'Importe des données depuis un fichier JSON dans la base de données'

    def handle(self, *args, **kwargs):
        # Ouvrir et lire le fichier JSON
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Importer les Enclos
        for enclos_data in data['enclos']:
            enclos, created = Enclos.objects.get_or_create(
                nom=enclos_data['nom'],
                defaults={
                    'description': enclos_data['description'],
                    'superficie': enclos_data['superficie']
                }
            )
            # Si l'enclos a été créé ou existe déjà, on met à jour l'image si elle est présente
            if 'image' in enclos_data and enclos_data['image']:
                enclos.image = enclos_data['image']
                enclos.save()
            
        # Importer les Soigneurs
        for soigneur_data in data['soigneurs']:
            Soigneur.objects.get_or_create(
                nom=soigneur_data['nom'],
                defaults={
                    'experience': soigneur_data['experience'],
                    'description': soigneur_data['description']
                }
            )
            
        # Importer les Animaux
        for animal_data in data['animaux']:
            enclos = Enclos.objects.get(nom=animal_data['enclos'])
            soigneur = None
            if 'soigneur' in animal_data:
                soigneur = Soigneur.objects.get(nom=animal_data['soigneur'])
            
            date_naissance = datetime.strptime(animal_data['date_naissance'], "%Y-%m-%d").date()
            date_arrivee = datetime.strptime(animal_data['date_arrivee'], "%Y-%m-%d").date() if 'date_arrivee' in animal_data else None

            animal, created = Animal.objects.get_or_create(
                nom=animal_data['nom'],
                defaults={
                    'description': animal_data['description'],
                    'enclos': enclos,
                    'soigneur': soigneur,
                    'date_naissance': date_naissance,
                    'date_arrivee': date_arrivee
                }
            )
            if 'image' in animal_data and animal_data['image']:
                animal.image = animal_data['image']
                animal.save()

        # Importer les Événements
        for evenement_data in data['evenements']:
            event_date_str = evenement_data['date']
            event_time_str = evenement_data['heure']
            evenement_date = datetime.strptime(f"{event_date_str} {event_time_str}", "%Y-%m-%d %H:%M")

            enclos = Enclos.objects.get(nom=evenement_data['enclos'])

            Evenement.objects.get_or_create(
                nom=evenement_data['nom'],
                defaults={
                    'description': evenement_data['description'],
                    'date': evenement_date,
                    'enclos': enclos
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Les données ont été importées avec succès!'))
