'''
Find the Gap Ups in the market
'''

from yahoo_finance import *
from pprint import pprint
import datetime

def GapUps(ticker, day_gap):
	yahoo = Share("%s" % ticker)

	today = datetime.date.today()
	start_day = today - datetime.timedelta(days=day_gap)
	closings = (yahoo.get_historical('%s' % start_day, '%s' % today))
	
	print(ticker)
	print(yahoo.get_open())

	for price in closings:
		pass
		#print(closings['Adj_Close'])
	print("---------------------------------")
'''
NASDAQ = open("NASDAQ.txt").read().splitlines()
NASDAQ = sorted(NASDAQ)
for stock in NASDAQ:
	ticker = stock.split(" ")[0]
	try:
		GapUps(ticker, 3)
	except:
		print("%s does not work" % ticker)
'''
GapUps("AAPL", 3)