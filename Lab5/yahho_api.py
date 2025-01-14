# -*- coding: utf-8 -*-
"""Yahho_API.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MfL5gJ3jEtbGk0nrL6vNMXucwne5JmHs
"""

!pip install yfinance

import yfinance as yf
import pandas as pd

ticker = 'TSLA'
ticker_data = yf.Ticker(ticker)
ticker_data

data = yf.download(ticker, start='2013-01-01',end='2023-01-01')
data

data = data[['Adj Close']]
data.reset_index(inplace = True)
data.columns = ['Date','Adj_Close']
data

daily_returns = [None]
for i in range(1, len(data)):
  per_change = (data['Adj_Close'][i] - data['Adj_Close'][i-1])/data['Adj_Close'][i-1]
  daily_returns.append(per_change)
daily_returns

data['Daily_Returns'] = daily_returns
data

data.dropna(inplace=True)
data.head()

!pip install hmmlearn numpy

from hmmlearn.hmm import GaussianHMM
import numpy as np

returns = data['Daily_Returns'].values
returns = returns.reshape(-1, 1)
returns

model = GaussianHMM(n_components=2, covariance_type="full", n_iter=1000, random_state = 42)
model.fit(returns)

hidden_states = model.predict(returns)
data['Hidden_State'] = hidden_states
data.head()

for state in range(model.n_components):
  print(f"Hidden State {state}")
  print(f"Mean: {model.means_[state][0]}")
  print(f"Variance: {np.diag(model.covars_[state])[0]}")

!pip install matplotlib

import matplotlib.pyplot as plt

plt.figure(figsize=(15,6))
for state in range(model.n_components):
  mask = (data['Hidden_State'] == state)
  plt.scatter(data['Date'][mask], data['Daily_Returns'][mask], label=f"state {state}", s=10)
plt.legend()
plt.xlabel("Date")
plt.ylabel("Daily Returns")
plt.title("Hidden States over Time")
plt.show()

print("Transition Matrix:")
print(model.transmat_)

plt.figure(figsize=(15,6))
plt.plot(data['Date'], data['Adj_Close'], label='Adjusted Close Price', color='red')

for state in range(model.n_components):
  mask = (data['Hidden_State'] == state)
  plt.fill_between(data['Date'][mask], data['Adj_Close'].min(), data['Adj_Close'].max(), alpha=0.3, label=f"state {state}")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.title("Stock Prices with Hidden Market Regimes")
plt.show()

curr_state = hidden_states[-1]
next_state_probability = model.transmat_[curr_state]
next_state = np.argmax(next_state_probability)

print(f"Current State: {curr_state}")
print(f"Transition probabilities: {next_state_probability}")
print(f"Next State: {next_state}")

"""# Predicting Bull or Bear in 2 state model"""

state_labels = []
for state in range(model.n_components):
  state_mean = model.means_[state][0]
  state_variance = np.diag(model.covars_[state][0])
  if state_mean > 0 and state_variance<0.001:
    state_label = 'Bull'
  elif state_mean<0:
    state_label = 'Bear'
  else:
    state_label = 'Neutral'
  state_labels.append(state_label)

data['Market_type'] = data['Hidden_State'].apply(lambda x: state_labels[x])
print(data[['Date', 'Adj_Close', 'Daily_Returns', 'Hidden_State', 'Market_type']].head())

plt.figure(figsize=(15,6))
plt.plot(data['Date'], data['Adj_Close'], label='Adjusted Close Price', color='red')
for state in range(model.n_components):
  mask = (data['Hidden_State'] == state)
  plt.fill_between(data['Date'][mask], data['Adj_Close'].min(), data['Adj_Close'].max(), alpha=0.3, label=f"state {state}")

plt.legend()
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.title("Stock Prices with Bull and Bear Market Types")
plt.show()