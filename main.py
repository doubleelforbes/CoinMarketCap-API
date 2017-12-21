# API Interface for CoinMarketCap.com
# Python Dependencies
import json
import urllib.request
#Self Dependencies
import cmccoin

def getAPIdata():
    requrl = "https://api.coinmarketcap.com/v1/ticker/?convert=GBP"
    response = urllib.request.urlopen(requrl).read()
    data = response.decode('utf-8')
    jsondata = json.loads(data)
    return jsondata

def getCoinIndex(coinstr):
    global coins
    i = 0
    for coin in coins:
        if coinstr.upper() == coin.Symbol:
            return i
        else:
            i += 1
    return -1

coins = []
print("Fetching API Data from https://api.coinmarketcap.com ...")
apidata = getAPIdata()
print("Data retreived, filling coin objects")
if "error" not in apidata:
    for item in apidata:
        cid = str(item.get("id"))
        name = str(item.get("name"))
        symbol = str(item.get("symbol"))
        rank = str(item.get("rank"))
        price_usd = str(item.get("price_usd"))
        price_btc = str(item.get("price_btc"))
        volusd24h = str(item.get("24h_volume_usd"))
        marketcapusd = str(item.get("market_cap_usd"))
        available_supply = str(item.get("available_supply"))
        total_supply = str(item.get("total_supply"))
        max_supply = str(item.get("max_supply"))
        change1h = str(item.get("percent_change_1h"))
        change24h = str(item.get("percent_change_24h"))
        change7d = str(item.get("percent_change_7d"))
        last_updated = str(item.get("last_updated"))
        price_gbp = str(item.get("price_gbp"))
        volgbp24h = str(item.get("24h_volume_gbp"))
        marketcapgbp = str(item.get("market_cap_gbp"))
        tmpCoin = cmccoin.cmcCoin(cid, name, symbol, rank, price_usd, price_btc, volusd24h, marketcapusd,
                                  available_supply, total_supply, max_supply, change1h, change24h, change7d,
                                  last_updated, price_gbp, volgbp24h, marketcapgbp)
        coins.append(tmpCoin)
else:
    print("API Returned Error!!")
print("Coin Objects Filled! Iterate and Print")
# An example of coin data access
# coin.tocommas() is also available for a headerless printout
for coin in coins:
    print(coin.tostring())
print(str(getCoinIndex("bTc")))
