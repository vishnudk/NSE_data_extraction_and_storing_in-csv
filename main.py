from nsetools import Nse
import requests as re
import csv
import datetime 
import time
def function():
   t = 1
   while 1:
      time.sleep(t)
      data = get_nse_data()
      if data!=None:
         enter_data_to_csv(data)
         t = 10
      else:
         t = 1


def get_nse_data():
   # headers = {
       
   #  'User-Agent': 'Chrome/ 86.0.4240.193'
   # }
   headers = {
       
    'User-Agent': 'Chrome/81.0.4044.138'
   }
   URL1 = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
   URL2 = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
   while 1:
      try:
         data_nifty = re.get(URL1,headers=headers).json()
         break
      except:
         break
   try:
      try:
         print(list(data_nifty['records']['data'][len(data_nifty['records']['data'])-1]['CE'].values()))
      except:
         print(list(data_nifty['records']['data'][0]['CE'].values()))
   except:
      return None
   # with open('nse_india_data.csv', 'w', newline='') as file:
   #    writer = csv.writer(file)
   #    writer.writerows(list([data_nifty['records']['data'][0]['PE'].keys()]))
   return list(data_nifty['records']['data'][0])

def enter_data_to_csv(data):
   dateandTime = datetime.datetime.now()
   data.append(dateandTime.strftime("%X"))
   data = list([data])
   with open('nse_india_data.csv', 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(data)


if __name__ == "__main__": 
   print(function())
