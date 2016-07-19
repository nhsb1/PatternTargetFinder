from argparse import ArgumentParser 
from yahoo_finance import Share
import pyperclip

currentrelease = 'Pattern Target Finder 1.1'
#v1.1 - Get's current delayed price from Yahoo_Finance
#		Allowed you to override price -p 123
#		Copies output to the clipboard
#v1.0 - calculates the pattern's target


def getArgs():
    parser = ArgumentParser(description = currentrelease)
    parser.add_argument("-t", "--ticker", required=False, dest="ticker", help="ticker for lookup", metavar="ticker")
    parser.add_argument("-p", "--price", required=False, dest="price", help="specify price", metavar="high")
    parser.add_argument("-rh", "--high", required=True, dest="high", help="recent high", metavar="high")
    parser.add_argument("-rl", "--low", required=True, dest="low", help="recent low", metavar="low")
    args = parser.parse_args()
    return args

def patternmove(high, low):
	move = float(high) - float(low)
	return move

def patterntarget(high, move):
	target = float(high) + float(move)
	return target

def priceWork(stock):
	"""
    Returns delayed price for ticker and reporting for ticker from Yahoo_Finance module (Yahoo_finance module delayed price can be VERY delayed, hence realtime module)
    """
	subpricequote = stock.get_price()
	#output.append(subpricequote)
	return subpricequote

#def clipboard1(ticker, price, move, target):



#----------------------------------------------------------------------
if __name__ == "__main__":
	myargs = getArgs()
	if myargs.ticker is not "" and myargs.price is None: #if you don't specify -p price then it get's the current delayed price
		stock = Share(myargs.ticker)
		price = priceWork(stock)
	elif myargs.ticker is not "" and myargs.price > 0: #if you specify price, then it uses that as the starting price.
		#print myargs.ticker, myargs.price
		stock = myargs.ticker
		price = myargs.price
	move = patternmove(myargs.high, myargs.low)
	target = patterntarget(myargs.high, move)
	#print target

	if myargs.ticker is not "" and price is not None:
		print myargs.ticker + ", " + str(price) + ", " + str(target)
		newpasteitem = myargs.ticker + ", " + str(price) + ", " + str(target)
		pyperclip.copy(newpasteitem)
	else:
		print target
		newpasteitem = str(target)
		pyperclip.copy(newpasteitem)

	
