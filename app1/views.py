from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def index(request):
    # the Task near the object is the title name of the class in models file
    tasks = Task.objects.all()
    form = TaskForm

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)

# def products(request):
#     return render(request, 'products.html')


# def contact(request):
#     return render(request, "contact.html")
