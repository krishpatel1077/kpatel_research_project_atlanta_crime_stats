#Krish Patel, 2020
import matplotlib.pyplot as plt
import csv

x = []
murder_new = []
murder_old = []
rape_new = []
rape_old = []
robbery_new = []
robbery_old = []
agg_ass_new = []
agg_ass_old = []

with open('DataSheetAtlanta.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        murder_new.append((row[1]))
        rape_new.append((row[2]))
        robbery_new.append((row[3]))
        agg_ass_new.append((row[4]))
        murder_old.append((row[5]))
        rape_old.append((row[6]))
        robbery_old.append((row[7]))
        agg_ass_new.append((row[8]))


plt.plot(x,murder_new, label='2019 Murder')
plt.plot(x,murder_old, label='2018 Murder')

plt.plot(x,rape_new, label='2019 Rape')
plt.plot(x,rape_old, label='2018 Rape')

plt.plot(x,robbery_new, label='2019 Robbery')
plt.plot(x,robbery_old, label='2018 Robbery')

plt.plot(x,agg_ass_new, label='2019 Aggravated Assault')
plt.plot(x,agg_ass_old, label='2018 Aggravated Assault')

plt.xlabel('Time (weeks)')
plt.ylabel('Cases (#)')
plt.title('Major Crime Rates - Atlanta 2018/2019')
plt.legend()
plt.show()