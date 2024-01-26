import market_information as info

fxInfo = info.FXInfo()
fx_rate = fxInfo.GetRate( "KRWUSD")

upbitInfo = info.UpbitInfo()
upbit_btc_price = upbitInfo.GetPrice("BTC/KRW")

bybitInfo = info.BybitInfo()
bybit_btc_price = bybitInfo.GetPrice("BTCUSD") * fx_rate

kimchi = upbit_btc_price - bybit_btc_price
kimch_rate = kimchi / bybit_btc_price * 100

print(f"FX Rate        : {fxInfo.GetRate( "KRWUSD") : > 14,}")
print()
print(f"UPBIT BTC PRC  : {int(upbit_btc_price) : > 12,}")
print(f"BYBIT BTC PRC  : {int(bybit_btc_price) : > 12,}")
print()
print(f"KIMCHI PREMIUM : {int(kimchi) : > 12,}")
print(f"KIMCHI RATE(%) : {kimch_rate : 12.2f}")

