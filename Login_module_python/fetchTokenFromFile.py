import csv
from datetime import datetime
import os.path
import config

def fetchTokenFromFile():
	file_exists = os.path.isfile(config.root_path+'access_token_file.csv')
	fieldnames = config.fieldnames
	with open(config.root_path+'access_token_file.csv', mode='r',newline='') as infile:
		reader = csv.DictReader(infile,fieldnames=fieldnames)
		for row in reader:
			dict = {'access_token': row['access_token'], 'time_stamp' :row['time_stamp']}
	return dict['access_token']