from django.http import HttpResponse

def home(request):
    return HttpResponse("Esta es la página principal del sitio.")
