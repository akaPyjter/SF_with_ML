import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

btc = pd.read_csv("../data/btc_1h.csv")
btc['avg'] = btc[['high', 'low']].mean(axis=1)
btc.drop(btc.columns[[0,2,3,4,5,6]],axis=1,  inplace=True)
btc.to_csv("../data/btc_1h_linear.csv")

btc = pd.read_csv("../data/btc_1h_linear.csv")
X = btc.iloc[:, 1].values
X = X.reshape(-1, 1)
y = btc.iloc[:, -1].values
y = y.reshape(-1, 1)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')

plt.show()