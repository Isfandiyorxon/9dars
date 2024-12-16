from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from .models import Gullar,Turlar
def home(request):
    gulllar=Gullar.objects.all()
    turlar=Turlar.objects.all()
    context={
        'turlar':turlar,
        'gullar':gulllar,
        'title':'Bosh sahifa'
    }
    return render(request,'hom.html',context)
def gul_by_tur(request,tur_id):
    gllar=Gullar.objects.filter(tur_id=tur_id)
    turlar=Turlar.objects.all()
    context={
        'gullar':gllar,
        'turlar':turlar
    }
    return render(request,'hom.html',context)

def gul_detail(request,pk):
    gul = get_object_or_404(Gullar, pk=pk)
    context={
        'gul':gul,
        'title':f"{gul.name}:batafsil"
    }
    return render(request,'index.html',context)