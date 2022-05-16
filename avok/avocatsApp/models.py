from django.db import models

GENDER = (
			('F', 'Feminin'),
			('M', 'Masculin'),
		)
ARRONDISSEMENT = (
    ('1er Arrondissement', '1er Arrondissemnt'),
    ('2eme Arrondissement', '2eme Arrondissemnt'),
    ('3eme Arrondissement', '3eme Arrondissemnt'),
    ('4eme Arrondissement', '4eme Arrondissemnt'),
    ('5eme Arrondissement', '5eme Arrondissemnt'),
    ('6eme Arrondissement', '6eme Arrondissemnt'),
    ('7eme Arrondissement', '7eme Arrondissemnt'),
    ('8eme Arrondissement', '8eme Arrondissemnt'),
    ('9eme Arrondissement', '9eme Arrondissemnt'),
    ('10eme Arrondissement', '10eme Arrondissemnt'),
)

# Create your models here.
class Clients(models.Model):
    idf= models.CharField('Identifiant', max_length=50)
    nom = models.CharField('Nom du Client', max_length=120)
    prenom = models.CharField('Prenom du  Client', max_length=120)
    sexe = models.CharField(choices=GENDER, null=True, max_length=10)
    adresse = models.CharField(choices=ARRONDISSEMENT, null=True, max_length=20)
    tel = models.CharField('Telephone du Client', max_length=120)
    profession = models.CharField('Profession du Client', max_length=50)

    def __str__(self):
        return self.nom

class Personnels(models.Model):
    #ide= models.CharField('Identifiant', max_length=50)
    nom = models.CharField('Nom du Personnel', max_length=120)
    prenom = models.CharField('Prenom du  Personnel', max_length=120)
    adresse = models.CharField('Adresse du Personnel', max_length=120)
    tel = models.CharField('Telephone du Personnel', max_length=120)
    email = models.EmailField("Email du Personnel", max_length=254)
    statut = models.CharField('Statut du Personnel', max_length=50)
    grade = models.CharField("Grade du Personnel", max_length=50)
    specialite = models.CharField('specialite du Personnel', max_length=50)

    def __str__(self):
        return self.nom

							
class Dossiers(models.Model):

    date = models.DateTimeField("Date de reception")
    statut = models.CharField("Statut du Dossier", max_length=50)
    categorie = models.CharField("Categorie du Dossier", max_length=50)
    description = models.TextField("Description")
    clients = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.statut

class Conseils(models.Model):
    
    date = models.DateTimeField("Date de reception")
    categorie = models.CharField("Categorie du Conseil", max_length=50)
    description = models.TextField("Description du Conseil")
    clients = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.categorie

class Redactions(models.Model):
    
    date = models.DateTimeField("Date de reception")
    categorie = models.CharField("Categorie de la Redaction", max_length=50)
    description = models.TextField("Description de la Redaction")
    clients = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.categorie
        