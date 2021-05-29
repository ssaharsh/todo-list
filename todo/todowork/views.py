from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


# Create your views here.

def show(request):
    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    return render(request,'show.html',context)

def home(request):
    context = {'success':False}
    if request.method=="POST":
        #handelling form
        Title = request.POST.get('Title')
        Desc = request.POST.get('Desc')

        #adding data to databae
        inst = Task(Title=Title,Desc = Desc)
        inst.save()
        context={'success':True}
    return render(request,'home.html',context)

def delete(request):
    # if request.method=='POST':
    #     Title = request.POST.get('Title')
    #     Desc = request.POST.get('Desc')
    #     task = Task.objects.get(Title=Title)
    #     task.delete()
    return render(request,'show.html')