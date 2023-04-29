import requests
from bs4 import BeautifulSoup
import webbrowser
def stock_data(said):
    if said in ("tell me about a stock","can you tell me about a stock"," can you tell me about the stock","tell me about a stock"):
        print("Processing stock data")
        ticker=str(input("Enter the stock Ticker/Symbol: "))
        #https://www.google.com/finance/quote/wonderla:NSE?hl=en
        url="https://www.google.com/finance/quote/"+ticker+":NSE?hl=en"
        webbrowser.open(url)
        
