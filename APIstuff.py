import requests
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

#DATA PROVIDED BY IEX CLOUD
with open('C:\\Users\\natet\\OneDrive\\Documents\\Python Scripts\\IEX_CLOUD_API_KEY.txt','r') as fi:
    API_KEY = fi.read()


API_VERSION = 'stable'
API_BASE = 'https://cloud.iexapis.com/'
FILE_PATH = 'C:\\Users\\natet\\OneDrive\\Documents\\Python Scripts\\'
#FILE_PATH = os.path.join('C:', 'users', 'natet', 'OneDrive', 'Documents', 'Python Scripts')
stocks = ['aapl', 'gm', 'aa', 'googl']

#load local stock list into code
def load_stock_list():
    with open(f'{FILE_PATH}stocks.json', 'r') as fi: 
        json.dump(stocks, fi)

#query api for current stock quote
def get_stock_quote(symb):
    r = requests.get(f'{API_BASE}/{API_VERSION}/stock/{symb}/quote?token={API_KEY}')
    return json.loads(r.content.decode('UTF-8'))

#update list in code
def get_stock_list():
    r = requests.get(f'https://api.iextrading.com/1.0/ref-data/symbols')
    current_stock_list = json.loads(r.content.decode('UTF-8'))
    for cs in current_stock_list:
        if cs["symbol"] not in stocks:
            stocks.update({cs["symbol"]:cs})

#update local list using list in code
def update_local_stock_list():
    with open(f'{FILE_PATH}stocks.json', 'w') as fo:
        json.dump(stocks, fo)

#gets stock price in a specified range
def get_stock_price(symb,range):
    r = requests.get(f'{API_BASE}/{API_VERSION}/stock/{symb}/chart/{range}?token={API_KEY}')
    return json.loads(r.content.decode('UTF-8'))

#updates a specific stock's data on local machine 
def save_stock_data(symb):
    with open(f'{FILE_PATH}\{symb}.json', 'w') as fo:
        json.dump(stock, fo)

#charts close data of a specific stock
def chart_stock_close(symb):
    with open(f'{FILE_PATH}\{symb}.json', 'r') as fi:
        df = pd.read_json(fi)
        cdf = df[['date', 'close']]
        cdf.plot(x='date', y='close')
        plt.xlabel("date")
        plt.ylabel("closing price")
        plt.show()

#for i in stocks:
#    s_data = get_stock_quote(i)
#    print(s_data['companyName'])


#stocks = {}
#get_stock_list()
#print(len(stocks))
#update_local_stock_list()
