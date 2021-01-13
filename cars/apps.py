from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'
    def redy(self):
    	import cars.signals