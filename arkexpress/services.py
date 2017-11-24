import requests
import json

from arkexpress import routers
from arkexpress import configs


class ClientAuth(object):

	def __init__(self, *args, **kwargs):
		self.__grant_type = kwargs.get('grant_type')
		self.__client_id = kwargs.get('client_id')
		self.__secret_key = kwargs.get('secret_key')

	def get_token(self):
		payload = {
			'grant_type': self.__grant_type,
			'client_id': self.__client_id,
			'secret_key': self.__secret_key
		}

		headers = {'Content-type': 'application/json'}

		r = requests.post(routers.ACCESS_TOKEN, data=json.dumps(payload), headers=headers)
		if r.status_code == configs.SUCCESS_CODE:
			return r.json()
		else:
			raise Exception('Error Response {}'.format(r.status_code))
		


class Shipment(ClientAuth):
	def __init__(self, *args, **kwargs):
		super(Shipment, self).__init__(*args, **kwargs)
		self.__reference_no = kwargs.get('reference_no')
		self.__waybill = kwargs.get('waybill')

	def get_info(self):
		auth = self.get_token()

		headers = {
			'Content-type': 'application/json',
			'Authorization': '{bearer} {token}'.format(
				bearer=auth.get('token_type'),
				token=auth.get('access_token'))
		}

		payload = [{
			'account_no': auth.get('account_no'),
			'reference_no': self.__reference_no,
			'waybill': self.__waybill
		}]

		r = requests.post(routers.SHIPMENT_INFO, data=json.dumps(payload), headers=headers)
		if r.status_code == configs.SUCCESS_CODE:
			return r.json()
		else:
			raise Exception('Error response {} on Shipment'.format(r.status_code))