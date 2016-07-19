# PatternTargetFinder 

![screenshot1](https://cloud.githubusercontent.com/assets/12847315/16967815/0d3dc982-4dd9-11e6-9794-25355399e54b.jpg)

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