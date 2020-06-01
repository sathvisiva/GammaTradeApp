
def read_one(fName):
	#start = time.time()
	column_list = ['Time','Open','High','Low','Close','v','vo']
	mylist = eval(open('C://Users//singh//Desktop//data_bot//'+fName, 'r').read())
	#print("Imported "+str(len(mylist['data']['candles']))+" items")
	mylist = mylist['data']['candles']
	df = pd.DataFrame(mylist,columns=column_list)
	#end = time.time()
	#print(f"Runtime of the program is {end - start}")
	return df

def read_all():
	start = time.time()
	file_list = os.listdir('C://Users//singh//Desktop//data_bot//')
	my_db = {}
	for i in range(len(file_list)):
		my_db[file_list[i]]=read_one(file_list[i])
	end = time.time()
	print(f"Loaded {len(file_list)} files in {end - start} secs")
	return my_db

def enter_position(entry_points,option_df):
	entry_points['Entry']=entry_points['High']
	entry_points['Exit']=0
	entry_points['Entry_Index']=0
	entry_points['Exit_Index']=0
	for i in range(len(entry_points)):
		index_entry_i = option_df.index[option_df['Time'] == entry_points['Time'][i]][0]
		entry_points['Entry_Index'][i]=index_entry_i
		for j in range(index_entry_i,len(option_df)):
			stop_loss = entry_points['Entry'][i] - 4
			target_price = entry_points['Entry'][i] + 10
			if option_df['High'][j] < stop_loss:
				entry_points['Exit'][i] = option_df['High'][j] 
				entry_points['Exit_Index'][i]=j
				break
			if option_df['High'][j] >= target_price:
				stop_loss = option_df['High'][j] - 2
	return entry_points

option_df = read_one("NIFTY20MAY9050CE.txt")

	entry_points=df_data.where(
		((df_data.shift(1)['Conv_line']-df_data.shift(1)['Base_line'])< 0) &
		(df_data['Low']>df_data['Lead_span_A']) & 
		((df_data['Conv_line']-df_data['Base_line'])> 0)
		)
	# entry_points = pd.DataFrame(entry_points['Time'].reset_index(drop=True))


	entry_points = pd.merge(option_df,entry_points,on='Time',how='right').dropna()

	count=0
	signal_set = []


	pnl = []
	count=0
	# for i in range(len(signal_set)):
	#     # aa=float(option_df.loc[df.Time == signal_set[i][1],'High']) - float(option_df.loc[df.Time == signal_set[i][0],'High'])
	#     try:
	#         profit = float(option_df.loc[option_df.Time == signal_set[count][1],'High']) - float(option_df.loc[option_df.Time == signal_set[count][0],'High'])
	#         pnl.append(profit)
	#         count=count+1
	#     except:
	#         pass

	# df.set_index("Time")

	end = time.time()
	print(f"Total time is {end - start}")