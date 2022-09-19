import yfinance as yf

ticker = yf.Ticker("CL=F")
print(ticker.info)