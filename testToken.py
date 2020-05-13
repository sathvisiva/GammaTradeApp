import csv
from datetime import datetime
import os.path
import config

file_exists = os.path.isfile(config.root_path+'access_token_file.csv')

fieldnames = config.fieldnames
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dict={fieldnames[0]:'testaccesstoken', fieldnames[1]: dt_string}

with open(config.root_path+'access_token_file.csv', mode='a',newline='') as outfile:
	writer = csv.DictWriter(outfile,fieldnames=fieldnames)
	if not file_exists:
		writer.writeheader()
	writer.writerow(dict)
