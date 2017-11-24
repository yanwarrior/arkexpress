import json

from arkexpress import services


class ArkExpress(object):
	SERVICE_SHIPMENT = 'SHIPMENT'

	def __init__(self, *args, **kwargs):
		self.__service = None
		if kwargs.get('service') == self.SERVICE_SHIPMENT:
			self.__service = services.Shipment
		else:
			raise Exception('Service not available.')

	@property
	def service(self):
		return self.__service
