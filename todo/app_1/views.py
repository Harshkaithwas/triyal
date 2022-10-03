from django.shortcuts import render,redirect
from . models import todos
from .forms import todosForm
# Create your views here.



def home(request):
    if request.method =='POST':
        form = todosForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('./home', )
    else:
        form = todosForm()
    return render(request,'home.html',{'form':form})


def listViews(request):
    todo = todos.objects.all()
    if request.method=="POST":
        todo.is_completed=True
        todo.save()
        return redirect('listViews')
    else:
        return render(request, 'todos.html',{'todo':todo})
    


def detailsView(request,pk):
    todo= todos.objects.get(pk=pk)
    return render(request, 'details.html', {'todo':todo})



def completed(request):
    todo=todos.objects.filter(is_completed=True)
    if request.method=='GET':
        todo=todos.objects.filter(is_completed=True)
        return render(request, 'completed.html',{'todo':todo} )

def pendings(request):
    todo=todos.objects.filter(is_completed=False)
    if request.method=="POST":
        todo.is_done=True
        todo.save()
        return redirect('pendings')
    else:
        return render(request, 'pendings.html',{'todo':todo} )
        

def update(request, pk):
    todo = todos.objects.get(pk=pk)
    if request.method=='POST':
        todo=todos.is_completed=True
        todo.save()
        return redirect('todos')
    else:
        return render(request, 'todos,html', {'todo':todo})
    