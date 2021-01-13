from django.db import models
from buyrs.models import Buyer
# Create your models here.
class Car(models.Model):
	name = models.CharField(max_length=100)
	price = models.PositiveIntegerField()
	buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
	code = models.CharField(max_length=10,blank=True)
