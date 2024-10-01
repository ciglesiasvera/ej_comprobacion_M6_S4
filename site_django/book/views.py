from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse  

def index(request):
    return HttpResponse("Bienvenidos a mi sitio de libros")  

""" def home(request):
    return redirect('/admin/') """
    
def home(request):
    return render(request, 'book/index.html')
