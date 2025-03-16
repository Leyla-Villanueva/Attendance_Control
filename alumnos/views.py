from django.shortcuts import render

# Create your views here.
def ver_asistencia(request):
    return render(request, 'inicio.html')