from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer

@receiver(post_save,sender=User)

def create_buyer_save(sender,instance,created,**kwargs):
	print('sender',sender)
	print('instance',instance)
	print('created',created)
	if created:
		Buyer.objects.create(user=instance)