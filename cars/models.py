from django.db import models
from buyrs.models import Buyer
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid
# Create your models here.
class Car(models.Model):
	name = models.CharField(max_length=100)
	price = models.PositiveIntegerField()
	buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
	code = models.CharField(max_length=10,blank=True)

	def __str__(self):
		return f"{self.name}-{self.price}-{self.buyer}"

@receiver(pre_save,sender=Car)
def save(sender,instance,**kwargs):
	if instance.code=="":
		instance.code=str(uuid.uuid4()).replace("-","").upper()[:10]
	