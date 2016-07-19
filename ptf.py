from argparse import ArgumentParser 

currentrelease = 'Pattern Target Finder 1.0'

def getArgs():
    parser = ArgumentParser(description = currentrelease)
    parser.add_argument("-rh", "--high", required=False, dest="high", help="recent high", metavar="high")
    parser.add_argument("-rl", "--low", required=False, dest="low", help="recnet low", metavar="low")
    args = parser.parse_args()
    return args

def patternmove(high, low):
	move = float(high) - float(low)
	return move

def patterntarget(high, move):
	target = float(high) + float(move)
	return target

#----------------------------------------------------------------------
if __name__ == "__main__":
	myargs = getArgs()
	move = patternmove(myargs.high, myargs.low)
	target = patterntarget(myargs.high, move)
	print target
	
