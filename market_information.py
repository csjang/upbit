import ccxt
import requests

##############################################################
# USD 환율 가져오기
##############################################################
class FXInfo:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    def __init__(self) -> None:
        pass

    def GetRate(self, fxCode) -> float:
        url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.' + fxCode
        exchange = requests.get(url, headers = self.headers).json()
        return float(exchange[0]['basePrice'])

##############################################################
# UPBIT 정보
##############################################################
class UpbitInfo:
    def __init__(self) -> None:
        self.upbit = ccxt.upbit()
        # upbit.load_markets()
        # self.symbols = upbit.symbols
        
    def GetPrice(self, symbol) -> float:
        mySymbols = ["BTC/KRW", "ETH/KRW", "XRP/KRW"]
        if (not symbol in mySymbols):
            return 0

        infos = self.upbit.fetch_ticker(symbol)
        return float(infos["close"])

##############################################################
# BYBIT 정보
##############################################################
class BybitInfo:
    def __init__(self) -> None:
        self.bybit = ccxt.bybit()
        # self.bybit.load_markets()
        # self.symbols = self.bybit.symbols
        
    def GetPrice(self, symbol) -> float:
        mySymbols = ["BTCUSD", "ETHUSD", "XRPUSD"]
        if (not symbol in mySymbols):
            return 0

        infos = self.bybit.fetch_ticker(symbol)
        return float(infos["close"])
 
    
if __name__ == "__main__":
    byInfo = BybitInfo()
    print(f"{byInfo.GetPrice("BTCUSD") : ,.2f}")
    # print(f"BTC/USD : {bybitInfo.GetPrice("BTCUSD") : > .2f }")
else:
    pass
    