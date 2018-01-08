
from core.models import User
from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(post_save, sender=User)
def print_user(sender, instance, created, **kwargs):
    print("Test signal receiver, it gets triggered when a user record is saved")
    print(sender)
    print(instance)
    print(kwargs)

