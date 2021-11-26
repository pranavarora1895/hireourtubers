from django.shortcuts import redirect, render
from .models import Contacttuber
from django.contrib import messages
# Create your views here.

def contacttuber(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']    
        subject = request.POST['subject']
        message = request.POST['message']

        contact_t = Contacttuber(name=name, phone=phone, email=email, subject=subject, message=message)
        contact_t.save()
        messages.success(request, 'Thanks for reaching out to us!!')
        return redirect('home')



