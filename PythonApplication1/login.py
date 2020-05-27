import requests
import logging
from kiteconnect import KiteConnect
from urllib.parse import urlparse
import json
import urllib
import csv
import config
import hashlib
import testToken
import fetchTokenFromFile

def login_fn():
	#logging.basicConfig(level=logging.DEBUG)
	with open(config.root_path+'credentials.csv', mode='r') as infile:
		reader = csv.reader(infile)
		credential_dict = {rows[0]:rows[1] for rows in reader}

	api_key=config.api_key
	user_id=config.user_id
	password=config.password
	twofa_value=config.twofa_value
	api_secret=config.api_secret

	payload = 'password='+password+'&user_id='+user_id

	kite = KiteConnect(api_key=api_key)

	api_url = kite.login_url()
	login_url = config.login_url
	two_fa_url = config.two_fa_url

	headers = {
		'X-Kite-Version': '3',
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
	

	#data = kite.generate_session(str(request_token), api_secret=secret_api)
	#kite.set_access_token(data["access_token"])
	auth_url=config.auth_url
	session_str = api_key + request_token + api_secret
	checksum = hashlib.sha256(str.encode('utf-8')).hexdigest()
	payload3 = 'api_key='+api_key+'&request_token='+request_token+'&checksum='+checksum
	response3 = requests.request("POST", auth_url, headers=headers, data = payload3)
	
	if(response3.status_code == 200):
		#update global access once handled
		return "Login Success"
	else :
		testToken.testToken()
		config.access_token=fetchTokenFromFile.fetchTokenFromFile()
		return "Login Fail "+str(response3.status_code)+fetchTokenFromFile.fetchTokenFromFile()