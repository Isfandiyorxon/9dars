from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GulForm
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

def add_gul(request):
    if request.method == 'POST':
        form=GulForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            gul=form.create()
            return redirect('detail',pk=gul.pk)
        else:
            print(form.errors)
        # else:
        #     print(form.errors)
        #     context = {
        #         'form': form
        #     }
        #     return render(request, 'add_gul.html', context)
    else:
        form=GulForm()
    context={
        'form':form
    }
    return render(request,'add_gul.html',context)
def gul_update(request,pk):
    gul=get_object_or_404(Gullar,pk=pk)
    if request.method=='POST':
        form=GulForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            gul.name=form.cleaned_data.get("name")
            gul.color=form.cleaned_data.get("color")
            gul.tur=form.cleaned_data.get("tur")
            gul.photo=form.cleaned_data.get("photo") if form.cleaned_data.get("photo") else gul.photo
            gul.about=form.cleaned_data.get("about")
            gul.save()
            return redirect('detail',pk=gul.pk)


    form=GulForm(initial={
         "name": gul.name,
        "about":gul.about,
        "photo":gul.photo,
        "tur":gul.tur,
        "color":gul.color
    })
    context={
        "form":form,
        "gul":gul
        }
    return render(request,'add_gul.html',context)



def delete_gul(request,pk):
    gul=get_object_or_404(Gullar, pk=pk)
    print("salom")
    if request.method=='POST':
        gul.delete()
        return redirect('home')
    context={
        'gul':gul
    }
    return render(request,'gul_delete.html',context)