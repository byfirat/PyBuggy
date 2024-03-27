from django.shortcuts import render
from django.http import HttpResponse

def anasayfa(request):
    return HttpResponse("Merhaba, dünya!")

def iletisim(request):
    return render(request, "iletisim.html")