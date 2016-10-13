'''
Find the Gap Ups in the market
'''

from yahoo_finance import *
import datetime

def GapUps(ticker, day_gap):
	yahoo = Share("%s" % ticker)
	today = datetime.date.today()
	start_day = today - datetime.timedelta(days=day_gap)
	closings = (yahoo.get_historical('%s' % start_day, '%s' % today))
	print(ticker)

	Change = []
	for price in closings:
		price_close = float(price['Adj_Close'])
		price_open = float(price['Open'])
		price_gap = (price_close - price_open)/(price_open)*100
		
		if price_gap > 0:
			Change.append(price_gap)

	Notable = []
	if len(Change) == day_gap:
		Notable.append(ticker)
	for tick in Notable:
		print(tick)

NASDAQ = open("NASDAQ.txt").read().splitlines()
NASDAQ = sorted(NASDAQ)
for stock in NASDAQ:
	ticker = stock.split(" ")[0]
	try:
		GapUps(ticker, 3)
	except:
		print("%s does not work" % ticker)
