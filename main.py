from nsetools import Nse
import requests as re
import time 
def function():
   while 1:
      time.sleep(10)
      data = get_nse_data()
      enter_data_to_csv(data)

def get_nse_data():
   headers = {
    'User-Agent': 'Chrome/81.0.4044.138'
   }
   URL1 = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
   URL2 = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'

def enter_data_to_csv(data):
   pass 
	
if __name__ == "__main__": 
   print(function())
