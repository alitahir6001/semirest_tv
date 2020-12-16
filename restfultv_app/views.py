from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Show


# Create your views here.

def index(request):
    return render(request, "index.html")

def process(request):
# pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
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
    show =  Show.objects.get(id=id)
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/edit_show/{show.id}')
    else:
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