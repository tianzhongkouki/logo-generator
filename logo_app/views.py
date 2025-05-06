from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def logo_view(request):
    return render(request, "logo_app/index.html")
