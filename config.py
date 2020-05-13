import fetchTokenFromFile
import csv

root_path = 'C://GammaTradeApp//'
login_url = "https://kite.zerodha.com/api/login"
two_fa_url = "https://kite.zerodha.com/api/twofa"
margins_url = "https://api.kite.trade/user/margins"
fieldnames = ['access_token', 'time_stamp']
access_token=fetchTokenFromFile.fetchTokenFromFile()

with open(root_path+'credentials.csv', mode='r') as infile:
	reader = csv.reader(infile)
	credential_dict = {rows[0]:rows[1] for rows in reader}

api_key=credential_dict["api_key"]
user_id=credential_dict["user_id"]
password=credential_dict["password"]
twofa_value=credential_dict["twofa_value"]
api_secret=credential_dict["api_secret"]