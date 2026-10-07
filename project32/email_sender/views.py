from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
# def sending_email(request):
#     print("Email Sent successfully!")
#     sub = 'Hi Yuvraj Sisodiya,'
#     msg = 'Welcome! Explore our website and discover something amazing.'
    
#     from_email = 'yuvrajsisodiyas19@gmail.com'
#     receiver_email = ['ys066893@gmail.com']

#     send_mail(sub , msg, from_email, receiver_email, fail_silently=False )

#     return HttpResponse("<h3>Email Sent Successfully</h3>")

def EmailMsg(request):
    html_content = render_to_string('welcome.html',{'username':'Rydham patel'})
    email = EmailMessage(
        subject='Welcome to My blog website',
        body=html_content,
        from_email='yuvrajsisodiyas19@gmail.com',
        to=['rydhampatel83@gmail.com']

    )
    email.content_subtype = "html"
    email.send()
    return HttpResponse("<h1>Html template gmail sent successfully</h1>")