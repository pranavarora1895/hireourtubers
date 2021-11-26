from django.core.mail.message import BadHeaderError
from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import mail_admins, send_mail
from .models import Hiretuber
from django.contrib import messages
# Create your views here.


def hiretuber(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name,
                              email=email, city=city, state=state, message=message, phone=phone, user_id=user_id)

        hiretuber.save()
        messages.success(request, 'Thanks for reaching out to us!!')
        subject = "Tuber Enquiry"
        body = {
            'first_name': first_name,
            'email': email,
            'message': message
        }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 'aurorapranav187@gmail.com',
                      ['aurorapranav187@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid Header Found.')
        return redirect('youtubers')
