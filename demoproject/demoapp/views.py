from django.shortcuts import render
from . import tasks
# Create your views here.

def test_view(request):
    return render(request, 'demo.html')

def submit(request):
    x = int(request.GET.get('num_1'))
    y = int(request.GET.get('num_2'))
    tasks.add.delay(x,y)
    
    return render(request, 'demo.html')