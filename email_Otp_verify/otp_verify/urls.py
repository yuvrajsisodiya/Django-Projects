from django.urls import path
from . import views
urlpatterns=[
    # # path("sending_email/",views.sending_email ,name='sending_email')
    # path("EmailMsg/",views.EmailMsg , name='EmailMsg')
    path("send_otp/", views.send_otp, name="send_otp"),
    path("verify_otp/", views.verify_otp, name="verify_otp"),
]