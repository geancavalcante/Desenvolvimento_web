from django.shortcuts import render

def pagina(request):
    return render(request,'index.html')

