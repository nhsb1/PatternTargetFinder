# PatternTargetFinder 
=====================================================
PatternTargetFinder calculates the target price for an equity based on the high (-rh), and low (-rl) that you pass to it from the shell.  Outputting to the command line and clipboard.


Install
-------

    Download the script

Usage
-----
   
    ptf.py [-h] [-t ticker] [-p high] -rh high -rl low

    Example: ptf.py -t oled -rh 77 -rl 33

Output
-----
   ticker, price, target

   Example: oled, 69.22, 107


Options
-----
    -h, --help          Print this help text and exit
    -rh, --high        	Specify a ticker symbol to run against (e.g. YHOO)
    -rl, --low         	Uses the Floor/Classic calculation
    -p, --price		Specifies an init. price 
    

See Also
--------

For more information: NA