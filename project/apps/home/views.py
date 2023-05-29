from django.shortcuts import render, redirect
from . import forms

def index(request):
    return render(request, "home/index.html")

def crear_tarea(request):
    if request.method == 'POST':
        form = forms.TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.TareaForm()
    return render(request, 'home/crear_tarea.html', {"form":form})

def crear_responsable(request):
    if request.method == 'POST':
        form = forms.ResponsableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.ResponsableForm()
    return render(request, 'home/crear_responsable.html', {"form":form})

def crear_local(request):
    if request.method == 'POST':
        form = forms.LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.LocalForm()
    return render(request, 'home/crear_local.html', {"form":form})
