CoinMarketCap.com API Access
============================

main.py has been set to call the getAPIdata() function and handle the returned json object.
The fields for each item are populated into a cmcCoin object List for easier access, iteration
and friendlier variable names.
=============================

cmcCoin Object
==============
Variables :
	self.Id = CoinMarketCap Unique ID
        self.Name = Real Name
        self.Symbol = ISO Symbol
        self.Rank = CoinMarketCap Rank
        self.PriceGBP = GBP Price
        self.VolumeGBP = GBP Volume
        self.MarketCapGBP = GBP Market Cap
        self.PriceUSD = USD Price
        self.VolumeUSD = USD Volume
        self.MarketCapUSD = USD Market Cap
        self.PriceBTC = BTC Price
        self.AvailableSupply = Available Supply
        self.TotalSupply = Total Supply
        self.MaxSupply = Maximum Supply
        self.ChangeHour = 1 Hour Change (Percent)
        self.ChangeDay = 1 Day Change (Percent)
        self.ChangeWeek = 7 Day Change (Percent)
        self.TimeStamp = Data Last Updated (Unix Timestamp: See tocommas() for conversion)
Methods :
	tostring()
		Returns : Header string followed by tocommas()
	tocommas()
		Returns : comma delimited variables