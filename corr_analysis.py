#IMPORTED CODE FROM POWER BI PYTHON SCRIPT***
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script:

# dataset = pandas.DataFrame(Incarceration Rate, Average Daily Population (ADP))
# dataset = dataset.drop_duplicates()

import pandas as pd
import matplotlib.pyplot as plt

data=dataset
data.columns = data.columns.str.replace(' ', '_')

#scaled the variables for fitting purposes
filtered_data = data[(data['Average_Daily_Population_(ADP)'] <= 500) & (data['Incarceration_Rate'] <= 10)]

#pearson correlation on filtered data
correlation = filtered_data['Average_Daily_Population_(ADP)'].corr(filtered_data['Incarceration_Rate'])
print(f'Pearson correlation coefficient: {correlation}')

# plotting the filtered data
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Average_Daily_Population_(ADP)'], filtered_data['Incarceration_Rate'], color='blue', marker='o')

plt.xlabel('Average Daily Population (ADP)')
plt.ylabel('Incarceration Rate')
plt.title(f'ADP vs. Incarceration Rate (Filtered Data)\nCorrelation: {correlation:.2f}')
plt.grid(True)

plt.show()