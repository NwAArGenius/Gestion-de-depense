from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Depense, Revenue
import plotly.graph_objs as go
import plotly.io as pio
from django.http import HttpResponse

# Create your views here.

user = get_user_model()

def home(request):
    return render(request, "home.html")


def CreateDepense(request):
    user = request.user 
    if request.method == 'POST':
        depense = Depense.objects.create(
            user=user,
            name=request.POST.get("name"),
            montant=request.POST.get("montant"),
            categorie=request.POST.get("categories")
        )
        return redirect("depenseUser")
    return render(request, 'createDepense.html')

def ReadDepense(request):
    user = request.user
    try:
        depense = Depense.objects.filter(user=user)
        revenue_total = sum([i.montant for i in depense])
        gap = revenue_total 
        context = {'depense': depense, "gap": gap}
        return render(request, 'depenseUser.html', context)
    except Depense.DoesNotExist:
        raise Http404("Aucun depense pour cette user")
    
def updateDepense(request, id):
    user = request.user 
    depense = Depense.objects.get(id=id)
    if request.method == 'POST':
        depense.name = request.POST.get("name")
        depense.montant = request.POST.get("montant")
        depense. categorie = request.POST.get("categories")
        depense.save()
        return redirect("depenseUser")
    return render(request, 'updateD.html', {'depense': depense})


def deleteDepense(request, id):
    user = request.user
    try:
        depense = Depense.objects.get(id=id)
    except Depense.DoesNotExist:
        # Handle the case where the Depense object does not exist
        return HttpResponse("Depense not found", status=404)
    else:
        depense.delete()
        return redirect('depenseUser')

            

def CreateRevenue(request):
    user = request.user
    if request.method == 'POST':
        revenue = Revenue.objects.create(
            user=user,
            name=request.POST.get("name"),
            montant=request.POST.get("montant"),
            categorie=request.POST.get("categories")
        )
        return redirect('revenueUser')
    return render(request, 'createRevenue.html')

def ReadRevenue(request):
    user = request.user 
    try:
        revenue = Revenue.objects.filter(user=user)
        revenue_total = sum([i.montant for i in revenue])
        gap = revenue_total 
        context = {"revenue": revenue, "gap": gap}
        return render(request, "RevenueUser.html", context)
    except Revenue.DoesNotExist:
        raise Http404("accun Revenue")
    
def updateRevenue(request, id):
    user = request.user 
    revenue = Revenue.objects.get(id=id)
    if request.method == 'POST':
        revenue.name = request.POST.get('name')
        revenue.montant = request.POST.get('montant')
        revenue.categorie = request.POST.get('categories')
        revenue.save()
        return redirect('revenueUser')
    return render(request, 'updateR.html', {'revenue': revenue})

def deleteReveneu(request, id):
    revenue = Revenue.objects.get(id=id) 
    revenue.delete()
    return redirect('revenueUser')
        
    
    

def gap_view(request):
    user = request.user
    depenses = Depense.objects.all()
    revenues = Revenue.objects.all()
    depense_total = sum([e.montant for e in depenses])
    revenue_total = sum([i.montant for i in revenues])
    gap = revenue_total - depense_total

    # Create Plotly figure
    fig = go.Figure(go.Bar(x=['Revenues', 'Dépenses'], y=[revenue_total, depense_total]))

    # Convert Plotly figure to HTML and pass to template
    graph_html = pio.to_html(fig, full_html=False)
    context = {'graph_html': graph_html}

    # Return rendered template
    return render(request, 'gap.html', context)

  
