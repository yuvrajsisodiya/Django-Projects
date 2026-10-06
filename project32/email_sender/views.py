from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def sending_email(request):
    sub = 'Welcome to my website'
    msg = 'Hello user, welcome to my website'
    
    from_email = 'yuvrajsisodiyas19@gmail.com'
    receiver_email = ['rydhampatel83@gmail.com']

    send_mail(sub , msg, from_email, receiver_email, fail_silently=False )

    return HttpResponse("<h3>Email Sent Successfully</h3>")