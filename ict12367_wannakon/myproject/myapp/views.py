from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Person
from django.db.models import Q  

def index(request):
    query = request.GET.get('q')

    if query:
        all_Person = Person.objects.filter(
            Q(name__icontains=query)
        )
    else:
        all_Person = Person.objects.all()

    return render(request, 'index.html', {
        "all_person": all_Person,
        "query": query
    })


def about(request):
    return render(request, 'about.html')


def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        Person.objects.create(
            name=name,
            age=age
        )

        return redirect("/")
    else:
        return render(request, 'form.html')


#  ต้องอยู่นอก form
def edit_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        person.name = name
        person.age = age
        person.save()

        return redirect("/")
    else:
        return render(request, 'edit.html', {"person": person})


def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")