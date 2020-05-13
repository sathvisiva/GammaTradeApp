import config

def checkLogin():
	with open(config.root_path+'access_token_file.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])