from nsetools import Nse
import requests as re
import csv
from datetime import date
import datetime 
import time
def function():
   t = 1
   while 1:
      # time.sleep(t)
      data = get_nse_data()
      if data!=None:
         enter_data_to_csv(data)
         break
      #    t = 10
      # else:
      #    t = 1


def get_nse_data():
   # print("get data function")
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
         # print("got the data ")
         break
      except:
         pass 
         # break
   # for i in data_nifty['records']['data']:
   #    print(i)
   #    print("==============")
   # # print("got out of the loop and now goig to prosecess the data and then to save it in the csv file")
   # try:
   #    try:
   #       print(list(data_nifty['records']['data'][len(data_nifty['records']['data'])-1]['CE'].values()))
   #    except:
   #       print(list(data_nifty['records']['data'][0]['CE'].values()))
   #    print("got the value")
   # except:
   #    return None
   # # with open('nse_india_data.csv', 'w', newline='') as file:
   # #    writer = csv.writer(file)
   # #    writer.writerows(list([data_nifty['records']['data'][0]['PE'].keys()]))
   # # return list(data_nifty['records']['data'][0])
   return data_nifty

def enter_data_to_csv(data):
   time = datetime.datetime.now()
   today = date.today()
   date1 = today.strftime("%b-%d-%Y")
   for i in (data['records']['data']):
      in_val = list([i['strikePrice'],i['expiryDate']])
      peData = [""]*19
      ceData = [""]*19
      try:
         print("PE")
         tmpdata = i['PE'].values()
         if tmpdata!="":
            peData = list(tmpdata)
            print(peData)
      except:
         pass
      try:
         print("CE")
         tmpdata = i['CE'].values()
         if tmpdata!="":
            ceData = list(tmpdata)
            print(ceData)
      except:
         pass
      peData.extend(ceData)
      peData.append(date1)
      peData.append(time.strftime("%X"))
      in_val.extend(peData)
      peData =  list([in_val])
      print("full data with appended date and time")
      print(peData)
      with open('nse_india_data.csv', 'a', newline='') as file:
         writer = csv.writer(file)
         writer.writerows(peData)
      print("=============")
   # for i in data['records']['data']:
   #    print(i)
   #    print("============================================")
   # dateandTime = datetime.datetime.now()
   # data.append(dateandTime.strftime("%X"))
   # data = list([data])
   # with open('nse_india_data.csv', 'a', newline='') as file:
   #    writer = csv.writer(file)
   #    writer.writerows(data)


if __name__ == "__main__": 
   print(function())
