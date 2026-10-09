from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User

@receiver(post_save , sender=User)
def welcome_send_email(sender , instance , created , **kwargs):
    if created:
        send_mail(
            subject = 'Welcome to Blog Application',
            message= f'Hi ,{instance.username},\n\n Welcome to My Blog application\n\nWe are happy to have you here.\n\nOur website is designed to provide useful information, helpful services, and a simple user-friendly experience. \n\nExplore different sections of our website, discover new things, and find everything you need in one place. ',
            from_email = 'yuvrajsisodiyas19@gmail.com',
            recipient_list = [instance.email],
        )
        print(f"Welcome Email sent to {instance.email} for user {instance.username}.")