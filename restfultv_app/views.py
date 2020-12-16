from django.shortcuts import render, HttpResponse, redirect
from .models import Show

# Create your views here.

def index(request):
    return render(request, "index.html")

def process(request):
    show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['releasedate'], description=request.POST['description'])
    return redirect(f'/view_show/{show.id}')


def view_show(request, id):
    
    context = {
        # 'all_shows': Show.objects.all(),
        # 'show': Show.objects.get(id=id),
        'show': Show.objects.all().filter(id=id)
    }
    return render(request, "view_show.html", context)

def shows(request):
    context = {
        "show": Show.objects.all(),
    }
    return render(request, "show.html", context)


def edit(request, id):
    show=Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['releasedate']
    show.description = request.POST['description']
    show.save()

    return redirect(f'/view_show/{show.id}')

def edit_show(request, id):
    context = {
    'show': Show.objects.get(id=id),
    }
    return render(request, 'edit.html', context)

def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')


# c = ClassName.objects.get(id=1)
# c.delete()