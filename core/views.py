from django.shortcuts import render
from django.http import HttpResponse
from . models import Contact

# Create your views here.
def home(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    msg = "";
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        msg = "Thank`s for your interest and time"

    context = {'contact':'active', 'msg':msg}
    return render(request, 'core/contact.html', context)