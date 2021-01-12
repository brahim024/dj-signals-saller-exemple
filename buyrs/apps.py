from django.apps import AppConfig


class BuyrsConfig(AppConfig):
    name = 'buyrs'
    def ready(self):
    	import buyrs.signals