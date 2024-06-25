#IMPORTED FROM POWER BI PYTHON SCRIPT
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script:

# dataset = pandas.DataFrame(Incarceration Rate, Average Daily Population (ADP))
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data=dataset
data.columns = data.columns.str.replace(' ', '_')

filtered_data = data[(data['Average_Daily_Population_(ADP)'] <= 500) & (data['Incarceration_Rate'] <= 10)]

correlation = filtered_data['Average_Daily_Population_(ADP)'].corr(filtered_data['Incarceration_Rate'])
print(f'Pearson correlation coefficient: {correlation}')

poly = PolynomialFeatures(degree=6)
X_poly = poly.fit_transform(filtered_data[['Average_Daily_Population_(ADP)']])
poly_reg = LinearRegression()
poly_reg.fit(X_poly, filtered_data['Incarceration_Rate'])

# predicting and plotting results
X_range = np.linspace(0, 500, 500).reshape(-1, 1)
y_poly_pred = poly_reg.predict(poly.fit_transform(X_range))

plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Average_Daily_Population_(ADP)'], filtered_data['Incarceration_Rate'],color='blue', marker='o')
plt.plot(X_range, y_poly_pred, color='red')
plt.xlabel('Average Daily Population (ADP)')
plt.ylabel('Incarceration Rate')
plt.title(f'ADP vs. Incarceration Rate (Polynomial Regression)\nCorrelation: {correlation:.2f}')
plt.grid(True)
plt.show()