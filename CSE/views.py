from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def admissions(request):
    return render(request, 'admissions.html')
    
def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')
