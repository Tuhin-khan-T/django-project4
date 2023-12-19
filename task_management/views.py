from django.shortcuts import render
from task.models import task 
def show_task(request):
     data = task.objects.all()
     
     return render(request, 'show_task.html',{'data' : data} )