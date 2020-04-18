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

plt.scatter(time, murder_new, label = "YTD 2019 Murder")
plt.scatter(time, murder_old, label = "YTD 2018 Murder")
plt.scatter(time, rape_new, label = "YTD 2019 Rape")
plt.scatter(time, rape_old, label = "YTD 2018 Rape")
plt.scatter(time, robbery_new, label = "YTD 2019 Robbery")
plt.scatter(time, robbery_old, label = "YTD 2018 Robbery")
plt.scatter(time, aggass_new, label = "YTD 2019 Aggravated Assault")
plt.scatter(time, aggass_old, label = "YTD 2018 Aggravated Assault")
plt.xlabel('Weeks of the Year')
plt.ylabel('# of Cases')
plt.title('Aggravated Assault Offenses in Atlanta 2018/19')
plt.legend()
plt.show()