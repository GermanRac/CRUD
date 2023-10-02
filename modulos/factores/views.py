from django.shortcuts import render
from . models import Indice
# Create your views here.

def home(request):
    IndicesListados = Indice.objects.all()
    return render(request,"gestionIndices.html",{"indices": IndicesListados})