from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Car
import uuid

'''
@receiver(pre_save,sender=Car)
def save(sender,instance,**kwargs):
	if instance.code=="":
		instance.code=str(uuid.uuid4()).replace("-","").upper()[:10]
	'''