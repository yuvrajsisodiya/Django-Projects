from django.urls import path
from . import views
urlpatterns=[
    # path("sending_email/",views.sending_email ,name='sending_email')
    # path("EmailMsg/",views.EmailMsg , name='EmailMsg')
    path("sending_mass_email/",views.sending_mass_email ,name='sending_mass_email')
]