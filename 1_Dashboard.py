import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("📈 Dashboard Marchés")

symbol = st.selectbox(
    "Choisir un actif",
    ["AAPL", "MSFT", "TSLA", "BTC-USD"]
)

stock = yf.Ticker(symbol)
data = stock.history(period="1d", interval="5m")

fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
))

fig.update_layout(template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)