# PySpams

## Program Description

**PySpams** is an alternative to [SPAms](http://compbio.igc.gulbenkian.pt/pcg/pcg_software.html) (Simulation Program for the Analysis of ms), which uses the ms program (Hudson, 2002).

SPAms converts the inputted parameters into ms commands and automatically runs the ms
program for the user. ([Readme PDF](http://compbio.igc.gulbenkian.pt/pcg/software/Readme.pdf))

**PySpams** is a platform independent program which can be used through a web interface.

It creates text files which can be used to perform IICR.
With PySpams you can also perform a simple IICR.


## WebInterface

This branch contains the necessary files to run PySpams on a browser.

There are several files:
* Python:
  * [______init____.py ](https://github.com/CarolinaPB/PySpams/blob/WebInterface/__init__.py)
  * [ms_IICR_functions.py](https://github.com/CarolinaPB/PySpams/blob/WebInterface/ms_IICR_functions.py): contains the functions needed to perform IICR


* HTML:

  * [main.html](https://github.com/CarolinaPB/PySpams/blob/WebInterface/templates/main.html): base page

  * [home.html](https://github.com/CarolinaPB/PySpams/blob/WebInterface/templates/home.html): homepage

  * [model1_form.html](https://github.com/CarolinaPB/PySpams/blob/WebInterface/templates/model1_form.html): where the user can create files with information related to the NSSC

  * [ms.html](https://github.com/CarolinaPB/PySpams/blob/WebInterface/templates/ms.html): where the user can perform a basic IICR
  * [fileexample.html](https://github.com/CarolinaPB/PySpams/blob/WebInterface/templates/fileexample.html): example of the file created by this program. The file used to perform IICR whould follow this structure


* CSS:

  * [bootstrap3.min.css](https://github.com/CarolinaPB/PySpams/blob/WebInterface/static/css/bootstrap3.min.css)


* Javascript:

  * [new_matrjs_alt.js](https://github.com/CarolinaPB/PySpams/blob/WebInterface/static/js/new_matrjs_alt.js): dynamically add fields to the form and save the file

  * [jquery-3.3.1.min.js](https://github.com/CarolinaPB/PySpams/blob/WebInterface/static/js/jquery-3.3.1.min.js)
  * [bootstrap.min.js](https://github.com/CarolinaPB/PySpams/blob/WebInterface/static/js/bootstrap.min.js)




## QTGui

This branch contains the necessary files to run PySpams in a Gui.

To use the Gui run [spams_alernative2.py](https://github.com/CarolinaPB/PySpams/blob/QtGui/spams_alternative2.py).
