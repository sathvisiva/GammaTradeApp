import time
import pandas as pd

def ichimoku_cloud_add(df_data):
	start = time.time()
	CL_period = 9 # length of Tenkan Sen or Conversion Line
	BL_period = 26 # length of Kijun Sen or Base Line
	Lead_span_B_period = 52 # length of Senkou Sen B or Leading Span B
	Lag_span_period = 26 # length of Chikou Span or Lagging Span

	df_data['Conv_line'] = (df_data.High.rolling(CL_period).max()+df_data.Low.rolling(CL_period).min())*0.5
	df_data['Base_line'] = (df_data.High.rolling(BL_period).max()+df_data.Low.rolling(BL_period).min())*0.5
	df_data['Lead_span_A'] = ((df_data['Conv_line'] + df_data['Base_line'])/2).shift(BL_period)
	df_data['Lead_span_B'] = ((df_data.High.rolling(Lead_span_B_period).max()+df_data.Low.rolling(Lead_span_B_period).min())/2).shift(BL_period)
	df_data['Lagging_span'] = df_data.Close.shift(-Lag_span_period)

	df_data.dropna(inplace=True)
	df_data=df_data.reset_index(drop=True)
	end = time.time()
	print(f"Total time for adding cloud = {end - start}")
	return df_data
