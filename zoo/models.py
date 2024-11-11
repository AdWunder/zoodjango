from django.db import models

class Soigneur(models.Model):
    nom = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Nombre d'années d'expérience")
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.nom

class Enclos(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    superficie = models.FloatField(help_text="Superficie en m²")
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Animal(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    enclos = models.ForeignKey('Enclos', on_delete=models.CASCADE)
    soigneur = models.ForeignKey('Soigneur', on_delete=models.CASCADE, null=True, blank=True)
    date_naissance = models.DateField()
    date_arrivee = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Evenement(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    enclos = models.ForeignKey(Enclos, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} - {self.date.strftime('%Y-%m-%d %H:%M')}"