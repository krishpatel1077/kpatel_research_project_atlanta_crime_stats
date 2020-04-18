#Krish Patel, 2020
from matplotlib import pyplot as plt
import pandas as pd
dataframe = pd.read_csv("DataSheetAtlanta.csv")

time = dataframe.WeeksoftheYear
murder_new = dataframe.YTD2019Murder
murder_old = dataframe.YTD2018Murder
rape_new = dataframe.YTD2019Rape
rape_old = dataframe.YTD2018Rape
robbery_new = dataframe.YTD2019Robbery
robbery_old = dataframe.YTD2018Robbery
aggass_new = dataframe.YTD2019AggAssault
aggass_old = dataframe.YTD2018AggAssault

plt.scatter(time, murder_new)
plt.scatter(time, murder_old)
plt.scatter(time, rape_new)
plt.scatter(time, rape_old)
plt.scatter(time, robbery_new)
plt.scatter(time, robbery_old)
plt.scatter(time, aggass_new)
plt.scatter(time, aggass_old)
plt.show()