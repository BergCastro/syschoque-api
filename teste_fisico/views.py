from django.shortcuts import render

# Create your views here.
def inscricoes_abertas(request):
    return render(request, 'tf_inscricoes_abertas.html')
