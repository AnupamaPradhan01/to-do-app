from django.shortcuts import render,HttpResponseRedirect
from .forms  import TodoRegistration
from .models import Todo


def home(request):
    if request.method=='POST':
        fm=TodoRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm=TodoRegistration()  
    else:
        fm=TodoRegistration()   
    todo=Todo.objects.all()       
    return render(request,"todoapp/home.html",{'todo':todo})

def delete(request,id):
    if request.method=='POST':
        pi=Todo.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update(request,id):
    if request.method=='POST':
        pi=Todo.objects.get(pk=id)
        fm=TodoRegistration(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi=Todo.objects.get(pk=id)
        fm=TodoRegistration(instance=pi)
    return render(request,'todoapp/update.html',{'form':fm})   

def mark_complete(request,id):
    pi=Todo.objects.get(pk=id)
    pi.completed=False
    pi.save()
    return HttpResponseRedirect('/')

def mark_incomplete(request,id):
    pi=Todo.objects.get(pk=id)
    pi.completed=True
    pi.save()
    return HttpResponseRedirect('/')           
    
