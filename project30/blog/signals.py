from django.db.models.signals import pre_save , post_save
from .models import BlogPost
from django.dispatch import receiver

# before saveing
@receiver(pre_save , sender=BlogPost)
def before_pre_save(sender,instance,**kwargs):
    # use of instance 
    print(f"About to save blog(pre_save)  : {instance.title}")

@receiver(post_save, sender=BlogPost)
def after_post_save(sender,created,instance,**kwargs):
    print(f"Post save run succesfully")
    if created:
        print("New blog created [post_save] : {instance.title}")

    else:
        print("Update blog created [post_save] : {instance.title}")

