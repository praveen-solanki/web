from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    
def Certifications(request):
    return render(request,'Certifications.html')

def Education(request):
    return render(request,'Education.html')

def Home(request):
    return render(request,'Home.html')

def Contact(request):
    return render(request,'Contact.html')

def Resume(request):
    return render(request,'Resume.html')

def interests(request):
    return render(request,'interests.html')

def Wip(request):
    return render(request,'Wip.html')
    
def Achievement(request):
    return render(request,'Achievement.html')

def Travelings(request):
    return render(request,'Travelings.html')


