from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request,'courses/index.html', context)

def add(request):
    if request.method=='POST':
        errors = {}
        if len(request.POST['name']) < 6:
            errors['name'] = "Course description should be more than 6 characters"
        if len(request.POST['description']) < 16:
            errors['description'] = "Course description should be more than 15 characters"
        if len(request.POST['name']) > 6 and len(request.POST['description']) > 16:
            Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    messages.error(request, "Course description should be more than 6 characters")
    messages.error(request, "Course description should be more than 15 characters")

    return redirect('/')

def delete(request,id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request,'courses/destroy.html',context)

def remove(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/')
