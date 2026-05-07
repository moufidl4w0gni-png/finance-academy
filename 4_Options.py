import streamlit as st
import numpy as np
import plotly.express as px

st.title("📗 Options")

strike = st.slider("Strike", 50, 200, 100)

prices = np.linspace(50, 200, 100)
payoff = np.maximum(prices - strike, 0)

fig = px.line(x=prices, y=payoff)

st.plotly_chart(fig, use_container_width=True)