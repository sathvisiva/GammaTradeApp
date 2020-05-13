import requests
import logging
from kiteconnect import KiteConnect
from urllib.parse import urlparse
import json
import urllib
import csv
import config

def login_fn():
	#logging.basicConfig(level=logging.DEBUG)
	with open(config.root_path+'credentials.csv', mode='r') as infile:
		reader = csv.reader(infile)
		credential_dict = {rows[0]:rows[1] for rows in reader}

	api_key=credential_dict["api_key"]
	user_id=credential_dict["user_id"]
	password=credential_dict["password"]
	twofa_value=credential_dict["twofa_value"]
	api_secret=credential_dict["api_secret"]

	payload = 'password='+password+'&user_id='+user_id

	kite = KiteConnect(api_key=api_key)

	api_url = kite.login_url()
	login_url = config.login_url
	two_fa_url = config.two_fa_url

	headers = {
	  'Content-Type': 'application/x-www-form-urlencoded'
	}

	my_session = requests.Session()
	response_login = my_session.request("POST", login_url, headers=headers, data = payload)

	json_data = json.loads(response_login.text)
	request_id=json_data['data']['request_id']
	payload2 = 'request_id='+request_id+'&twofa_value='+twofa_value+'&user_id='+user_id

	response = my_session.request("POST", two_fa_url, headers=headers, data = payload2)

	token_response=my_session.get(api_url)
	response_dict=dict(urllib.parse.parse_qsl(urlparse(token_response.url).query))
	request_token=response_dict["request_token"]
	success_flag=response_dict["status"]
	return request_token, success_flag

#data = kite.generate_session(str(request_token), api_secret=secret_api)
#kite.set_access_token(data["access_token"])
#profile_url="https://api.kite.trade/session/token"
#str=api_key + request_token + api_secret
#checksum = hashlib.sha256(str.encode('utf-8')).hexdigest()
#payload3 = 'api_key='+api_key+'&request_token='+request_token+'&checksum='+checksum
#response3 = requests.request("POST", profile_url, headers=headers, data = payload3)