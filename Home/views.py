from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime

def index(request):
    return render(request,"index.html")

def about(request):

    return render(request,"about.html")

def contact(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name,phone=phone,email=email,desc=desc, date=datetime.today())
        contact.save()
    return render(request,"contact.html")

def services(request):

    return render(request,"services.html")


def order(request):

    return render(request,"order.html")

 
    # return HttpResponse("this is Special Order page")


# Create your views here.
