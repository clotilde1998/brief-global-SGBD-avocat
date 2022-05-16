from django.shortcuts import render, redirect
from .models import Personnels, Clients, Dossiers, Conseils, Redactions
from django.http import HttpResponseRedirect
from .forms import ClientsForm, PersonnelsForm, DossiersForm, ConseilsForm, RedactionsForm

def home(request):
	return render(request, 'avocat/home.html', {})

def apropos(request):
    	return render(request, 'avocat/apropos.html', {})

def personnels_list(request):
    personnel = Personnels.objects.all().order_by('nom')
    return render(request, 'avocat/personnels_list.html', {
        'personnels': personnel,
    })



def clients_list(request):
    client = Clients.objects.all().order_by('nom')
    return render(request, 'avocat/clients_list.html', {
        'clients': client,
    })


def dossiers_list(request):
    dossier = Dossiers.objects.all().order_by('statut')
    return render(request, 'avocat/dossiers_list.html', {
        'dossiers': dossier,
    })


def client_add(request):
    submitted = False
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/client_add?submitted=True')
    else:
        form = ClientsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/client_add.html', {
	    'form': form,
	    'submitted': submitted,
})

def personnel_add(request):
    submitted = False
    if request.method == "POST":
        form = PersonnelsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/personnel_add?submitted=True')
    else:
        form = PersonnelsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/personnel_add.html', {
	    'form': form,
	    'submitted': submitted,
})

def dossier_add(request):
    submitted = False
    if request.method == "POST":
        form = DossiersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dossier_add?submitted=True')
    else:
        form = DossiersForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/dossier_add.html', {
		'form': form,
		'submitted': submitted,
})

def client_update(request, pk):
    client = Clients.objects.get(idf=pk)
    form = ClientsForm(instance=client)
    if request.method=='POST':
        form = ClientsForm(request.POST,instance=client)
    if form.is_valid():
            form.save()
            return redirect('client-list')
    context={'form':form}
    return render(request, 'avocat/client_add.html', context)

def personnel_update(request, pk):
    personnel = Personnels.objects.get(nom=pk)
    form = PersonnelsForm(instance=personnel)
    if request.method=='POST':
        form = PersonnelsForm(request.POST,instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('personnel-list')
    context={'form':form}
    return render(request, 'avocat/personnel_add.html', context)

def dossier_update(request, pk):
    dossier = Dossiers.objects.get(statut=pk)
    form = DossiersForm(instance=dossier)
    if request.method=='POST':
        form = DossiersForm(request.POST,instance=dossier)
    if form.is_valid():
            form.save()
            return redirect('dossier-list')
    context={'form':form}
    return render(request, 'avocat/dossier_add.html', context)


def client_delete(request, pk):
    client = Clients.objects.get(idf=pk)
    client.delete()
    return redirect('client-list')

def personnel_delete(request, pk):
    personnel = Personnels.objects.get(nom=pk)
    personnel.delete()
    return redirect('personnel-list')

def dossier_delete(request, pk):
    dossier = Dossiers.objects.get(statut=pk)
    dossier.delete()
    return redirect('dossier-list')


def conseils_list(request):
    conseil = Conseils.objects.all().order_by('categorie')
    return render(request, 'avocat/conseils_list.html', {
        'conseil': conseil,
    })

def redactions_list(request):
    redaction = Redactions.objects.all().order_by('categorie')
    return render(request, 'avocat/redactions_list.html', {
        'redaction': redaction,
    })


def conseil_add(request, pk):
    submitted = False
    if request.method == "POST":
        form = ConseilsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/conseil_add?submitted=True')
    else:
        form = ConseilsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/conseil_add.html', {
		'form': form,
		'submitted': submitted,
})

def redactions_add(request):
    submitted = False
    if request.method == "POST":
        form = RedactionsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/redactions_add?submitted=True')
    else:
        form = RedactionsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/redactions_add.html', {
		'form': form,
		'submitted': submitted,
})

'''def search_client(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q(Q(nom__icontains=query) | Q(prenom__icontains=query))
            client = Client.objects.filter(mutiple_q)
            if client:
                return render(request, 'client/clients_list.html', {
                    'client': client
                    })
                    else:
                        print('Not found ...')
                        return render(request, 'client/not_found.html', {})
                        '''
# Create your views here.
