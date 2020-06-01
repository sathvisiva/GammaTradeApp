import sys
sys.path.append('secret/')
sys.path.append('ichimoku/')

import datetime
import pandas as pd
import data_code
import ichimoku_cloud
print("this is a backtest module")

start_data=int((datetime.datetime(2020,4,1,9,15)).timestamp())
end_data=int((datetime.datetime(2020,5,1,15,30)).timestamp())
data_code.fetch_data(start_data,end_data)

data_my=data_code.get_data()

ichi_cloud = ichimoku_cloud.ichimoku_cloud_add(data_my)
