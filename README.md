# Infinalys2

Infinalys2 is the successor of the Infinalys project which was an artificial intelligence to make prediction of the trading market and currently on the project you have the recovery of trading information.

## Getting Started

### Prerequisites

## you must install python before going on
```
pip install yfinance --user
pip install pandas --user
pip install stockstats --user
pip install tensorflow --user
pip install matplotlib --user
```
## and frontend you must
```
cd front
npm install
npm start
```

## Overview

Move into src Folder and run main.py
```
./main.py (stock) (interval)
OR
python3 main.py (stock) (interval)
```
### USAGE
stock: stock symbol to be downloaded
interval: interval of the stock to be downloaded (1d, 5d, or 1mo)

##### EXAMPLES:
```
./main.py APPL 1d
./main.py OIL 5d
./main.py
./main.py AMZN 1mo
```

### Customisation

In the folder assets in irma folder you can see 2 file


In the companies.csv you got a list of the Best 506 companies in the trading market.

And you can copy in this file somme companies and put them into the file companies_test to evaluate them

the result of the fetch of companies_test is put into the ```stock ``` file

## Back_end

The back_end is done with flask we get request to be able transmit the purse and the candle time.

## Built With

* [yahoo-finance-api](https://github.com/topics/yahoo-finance-api) - Fetch framework used
* [stock-stats](https://github.com/jealous/stockstats) - Stocks indicators calculator
* [stockCharts](https://github.com/rrag/react-stockcharts) - chart lib in react
* [materialUI](https://material-ui.com/) - graphical framework in react
