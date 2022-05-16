from django.forms import ModelForm 
from .models import Clients, Personnels, Dossiers, Conseils, Redactions
from django.db.models import fields 
from django.db import models

class ClientsForm(ModelForm):
    class Meta:
	    model = Clients
	    fields = '__all__'

	    labels = {
			'ID':'',
		    'Nom': '',  
		    'Prenom': '',    
		    'Adresse': '',  
		    'Tel': '',
			'Sexe':'', 
		    'Profession': '',  
	    }
'''
	    #widgets = {
		    #'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom',}),  
		    #'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'prenom',}), 
		    #'adresse': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'adresse',}), 
		    #'tel': form.TextInput(attrs={'class': 'form-select', 'placeholder': 'tel',}),  
		    #'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'profession',}),  
								
	    #}
'''


class PersonnelsForm(ModelForm):
    class Meta:
	    model = Personnels
	    fields = '__all__'

	    labels = {
			
		    'Nom': '',  
		    'Prenom': '',    
		    'Adresse': '',  
		    'Tel': '', 
		    'Email': '',  
            'Statut': '',
			'Grade':'',
            'Specialite': '',
	    }
'''
	    widgets = {
		    'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom',}),  
		    'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'prenom',}), 
		    'adresse': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'adresse',}), 
		    'tel': form.TextInput(attrs={'class': 'form-select', 'placeholder': 'tel',}),  
		    'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email',}), 
            'statut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'statut',}), 
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'specialite',})				
	    }
'''

class DossiersForm(ModelForm):
    class Meta:
	    model = Dossiers
	    fields ='__all__'

	    labels = {
		    'Date': '',  
		    'Statut': '',    
		    'Categorie': '',
			'Description':'',  
		    'Client': '', 
		    'Personnel': '',  
	    }

class ConseilsForm(ModelForm):
    class Meta:
	    model = Conseils
	    fields ='__all__'

	    labels = {
		    'Date': '',      
		    'Categorie': '',
			'Description':'',  
		    'Client': '', 
		    'Personnel': '',  
	    }

class RedactionsForm(ModelForm):
    class Meta:
	    model = Redactions
	    fields ='__all__'

	    labels = {
		    'Date': '',    
		    'Categorie': '',
			'Description':'',  
		    'Client': '', 
		    'Personnel': '',  
	    }
'''
	    widgets = {
		    'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'date',}),  
		    'statut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'statut',}), 
		    'categorie': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'categorie',}), 
		    'client': form.TextInput(attrs={'class': 'form-select', 'placeholder': 'client',}),  
		    'personnel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'personnel',}),  
								
	    }
'''