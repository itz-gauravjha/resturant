from django.shortcuts import render, HttpResponse
from .models import BookTable, MenuItem
from .forms import BookTableForm


def home(request):
    menu_items = MenuItem.objects.all()
    return render(request,"home_app/home.html", context = {'menu_items':menu_items})

def about(request,):
    return render(request,"home_app/about.html")    

def contact(request):
    return render(request,"home_app/contact.html")    

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request,"home_app/menu.html", context = {'menu_items':menu_items})    




def order(request):
    if(request.method=="POST"):
        form = BookTableForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Booking Sucessful")
    else:
        return render(request,"home_app/order.html")

        