import config
import requests

def isLoggedIn():
	margins_url = config.margins_url
	payload = {}
	signing_str = 'token '+config.api_key+':'+config.access_token
	headers = {
	  'X-Kite-Version': '3',
	  'Authorization': signing_str,
	}

	response = requests.request("GET", margins_url, headers=headers, data = payload)

	if(response.status_code == 200):
		return True
	return False