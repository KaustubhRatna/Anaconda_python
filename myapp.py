import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of "MAANG" Companies!!

Created by Kaustubh Ratna

""")

st.write(""" ## Google """)
tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2022-5-31')



st.line_chart(tickerDf.Close)
st.bar_chart(tickerDf.Volume)

st.write(""" ## Apple """)
tickerSymbol1 = 'AAPL'

tickerData1 = yf.Ticker(tickerSymbol1)

tickerDf1 = tickerData1.history(period='1d',start='2010-5-31',end='2022-5-31')



st.line_chart(tickerDf1.Close)
st.bar_chart(tickerDf1.Volume)

st.write(""" ## Amazon """)
tickerSymbol2 = 'AMZN'

tickerData2 = yf.Ticker(tickerSymbol2)

tickerDf2 = tickerData2.history(period='1d',start='2010-5-31',end='2022-5-31')



st.line_chart(tickerDf2.Close)
st.bar_chart(tickerDf2.Volume)

st.write(""" ## Meta """)
tickerSymbol3 = 'META'

tickerData3 = yf.Ticker(tickerSymbol3)

tickerDf3 = tickerData3.history(period='1d',start='2010-5-31',end='2022-5-31')



st.line_chart(tickerDf3.Close)
st.bar_chart(tickerDf3.Volume)

st.write(""" ## Netflix """)
tickerSymbol4 = 'NFLX'

tickerData4 = yf.Ticker(tickerSymbol4)

tickerDf4 = tickerData4.history(period='1d',start='2010-5-31',end='2022-5-31')



st.line_chart(tickerDf4.Close)
st.bar_chart(tickerDf4.Volume)
