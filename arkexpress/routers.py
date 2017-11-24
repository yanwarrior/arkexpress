from arkexpress.configs import DEBUG_MODE

if DEBUG_MODE:
	BASE_URL = "https://api-dev.ark-xpress.com"
else:
	BASE_URL = "https://api.ark-xpress.com"

ACCESS_TOKEN = "{}/oauth/access_token".format(BASE_URL)
SHIPMENT_INFO = "{}/ext/v1/getshipmentsinfo".format(BASE_URL)



