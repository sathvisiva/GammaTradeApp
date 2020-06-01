import sys
sys.path.append('secret/')
import data_code
import datetime

print("this is a backtest module")

start_data=int((datetime.datetime(2020,4,1,9,15)).timestamp())
end_data=int((datetime.datetime(2020,5,1,15,30)).timestamp())
data_code.fetch_data(start_data,end_data)

print(data_code.get_data())
