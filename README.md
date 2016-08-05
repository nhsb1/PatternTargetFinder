![screenshot1](https://cloud.githubusercontent.com/assets/12847315/16967815/0d3dc982-4dd9-11e6-9794-25355399e54b.jpg)

=====================================================
PatternTargetFinder calculates the target price for an equity based on the high (-rh), and low (-rl) that you pass to it from the shell.  You can specify an init price, outputting to the command line and clipboard.  Specify earnings (-e), to get the upcoming earnings date.


Install
-------

    Download the script

Usage
-----
   
    ptf.py [-h] [-t ticker] [-p high] -rh high -rl low [-e]

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
    -t, --ticker        If you specify a ticker with no price, ptf.py wlil use Yahoo Finance to look it up
    -p, --price		Specifies an init. price.  If none is specified, but a ticker is specified, it will use Yahoo Finance to look it up.
    -e, --earnings	Gets earnings date    

See Also
--------

For more information: NA