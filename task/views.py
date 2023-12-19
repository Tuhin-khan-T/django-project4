

from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_task(request):
    if request.method == 'POST': # user post request koreche
        task_form = forms.taskForm(request.POST) # user er post request data ekhane capture korlam
        if task_form.is_valid(): # post kora data gula amra valid kina check kortechi
            task_form.save() # jodi data valid hoy taile database e save korbo
            return redirect('add_task') # sob thik thakle take add author ei url e pathiye dibo
    
    else: # user normally website e gele blank form pabe
        task_form = forms.taskForm()
    return render(request, 'add_task.html', {'form' : task_form})




def edit_task(request, id):
    Task = models.task.objects.get(pk=id) 
    task_form = forms.taskForm(instance=Task)
    print(Task.title)
    if request.method == 'POST': # user post request koreche
        task_form = forms.taskForm(request.POST,instance=Task) # user er post request data ekhane capture korlam
        if task_form.is_valid(): # post kora data gula amra valid kina check kortechi
            task_form.save() # jodi data valid hoy taile database e save korbo
            return redirect('show_task') # sob thik thakle take add author ei url e pathiye dibo
    
   # else: # user normally website e gele blank form pabe
       # task_form = forms.taskForm()
        
    return render(request, 'add_task.html', {'form' : task_form})



def delete_task(request, id):
    Task = models.task.objects.get(pk=id) 
    Task.delete()
    return redirect('show_task') 

