from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage , send_mass_mail
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

# def EmailMsg(request):
#     html_content = render_to_string('welcome.html',{'username':'Rydham patel'})
#     email = EmailMessage(
#         subject='Welcome to My blog website',
#         body=html_content,
#         from_email='yuvrajsisodiyas19@gmail.com',
#         to=['rydhampatel83@gmail.com']

#     )
#     email.content_subtype = "html"
#     email.send()
#     return HttpResponse("<h1>Html template gmail sent successfully</h1>")

def sending_mass_email(request):
    # 1st
    messages = (
    (
        'Welcome to My blog website',
        'Hi Rydham Patel , Welcome! Explore our website and discover something amazing.\n\nThank you for joining us!',
        'yuvrajsisodiyas19@gmail.com',
        [ 'rydhampatel83@gmail.com']
    ),
    # 2nd
    (
    'Update from My blog website',
    'Hi customer, We have some exciting updates and new features on our website. Check them out now!\n\n Thank you for being a valued member of our community.',
    'yuvrajsisodiyas19@gmail.com',
    ['rydhampatel83@gmail.com', 'ys066893@gmail.com' , 'yuvrajsisodiyas19@gmail.com']
    ),
    # 3rd
    (
        'Special Offer from My blog website',
        'Hi customer, We have a special offer just for you! Get 20% off your next purchase on website. Use the code SPECIAL20 at checkout.\n\nThank you for being a loyal customer!',
        'yuvrajsisodiyas19@gmail.com',
        ['rydhampatel83@gmail.com', 'ys066893@gmail.com' , 'yuvrajsisodiyas19@gmail.com']
    ),

    )
    send_mass_mail(messages)

    fail_silently=False
    return HttpResponse("<h3>Mass Email Sent Successfully</h3>")