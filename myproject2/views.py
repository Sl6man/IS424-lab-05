from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person
from .forms import PersonForm

people = []

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_person = Person(username=username, password=password)
            people.append(new_person)
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()
    return render(request, 'myapp/add.html', {'form': form})

def show_people(request):
    return render(request, 'myapp/show.html', {'people': people})
