# stacked bar chart to show the confirmed Indian and foreign national cases for the state Kerala and Tamil Nadu for a period of 1 week
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data1 = [['21/03/20', 'Kerala', 33,7],['22-03/20', 'Kerala',45,7 ],['23/03/20', 'Kerala',60,7],
['24/03/20', 'Kerala',87,8 ], ['25/03/20', 'Kerala',101,8 ], ['26/03/20', 'Kerala',110,8], ['27/03/20',
'Kerala', 129,8]]
data2=[['21/03/20', 'Tamil Nadu', 3,0], ['22/03/20', 'Tamil Nadu',5,2 ],['23/03/20', 'Tamil Nadu',7,2], ['24/03/20', 'Tamil Nadu',13,2 ], ['25/03/20', 'Tamil Nadu',16,2 ], ['26/03/20', 'Tamil Nadu',20,6], ['27/03/20', 'Tamil Nadu',23,6 ]]

df1 = pd.DataFrame(data1, columns = ['Date', 'State','Confirmed_indian_nationals',
'Confirmed_foreign_nationals'])
df_grouped1 = df1.groupby('Date').sum()
[['Confirmed_indian_nationals','Confirmed_foreign_nationals']]
df2 = pd.DataFrame(data2, columns = ['Date', 'State','Confirmed_indian_nationals',
'Confirmed_foreign_nationals'])
df_grouped2 = df2.groupby('Date').sum()
[['Confirmed_indian_nationals','Confirmed_foreign_nationals']]
fields = ['Confirmed_indian_nationals','Confirmed_foreign_nationals']
colors = ['#ee99a0', '#822659']
labels = ['Indian', 'Foreign']

fig, ax = plt.subplots(1, figsize=(12, 10))
left = len(df_grouped1) * [0]
for idx, name in enumerate(fields):
 plt.barh(df_grouped1.index, df_grouped1[name], left = left, color=colors[idx])
 left = left + df_grouped1[name]
plt.title('RIA ARUN - 19BCE2440 --- COVID CASES IN KERALA TIMELEINE \n', color='maroon', loc='left')
plt.legend(labels, bbox_to_anchor=([0.55, 1, 0, 0]), ncol=4, frameon=False)

plt.ylabel('Date')
plt.xlabel('Number of confirmed cases')
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.ylim(-0.5, ax.get_yticks()[-1] + 0.5)
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed')
plt.show()

left = len(df_grouped2) * [0]
for idx, name in enumerate(fields):
 plt.barh(df_grouped2.index, df_grouped2[name], left = left, color=colors[idx])
 left = left + df_grouped2[name]
plt.title('RIA ARUN - 19BCE2440 --- COVID CASES IN TAMILNADU TIMELEINE \n', color='maroon', loc='left')
plt.legend(labels, bbox_to_anchor=([0.65, 1, 0, 0]), ncol=4, frameon=False)

plt.ylabel('Date')
plt.xlabel('Number of confirmed cases')
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.ylim(-0.5, ax.get_yticks()[-1] + 0.5)
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed')
plt.show()



# data for cured and deaths in April to three states with mean, variance and correlation showing in the bottom of the table
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from statistics import mean
gf = pd.read_csv("/Users/Ria/Downloads/covid_19_india.csv")
y= (gf[gf["Month"]=="April"])
z1 = pd.DataFrame()
z1["Date"]=(y[y["State"]=="Kerala"]["Date"])
z1["Cured_Kerala"]=(y[y["State"]=="Kerala"]["Cured"])
z1["Deaths_Kerala"]=(y[y["State"]=="Kerala"]["Deaths"])
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
table1 = ax.table(cellText=z1.values, colLabels=z1.columns, loc='center')

print(table1)
print("Average is: ")
print(z1.mean(axis=0))
print("\nVariance is: ")
print(z1.var())
print("\nCorrelation is: ")
print(z1.corr(method ='pearson'))
z1.reset_index().plot(x="Date", y=["Cured_Kerala"], kind="bar")

plt.title("RIA ARUN - 19BCE2440 -- PLOT OF CURES")
plt.xlabel("Date")
plt.ylabel("No of people cured")
z1.reset_index().plot(x="Date", y=["Deaths_Kerala"], kind="bar")
plt.title("RIA ARUN - 19BCE2440 -- PLOT OF DEATHS")
plt.xlabel("Date")
plt.ylabel("No of deaths")

z1.reset_index().plot(x="Date", y=["Cured_Kerala","Deaths_Kerala"], kind="bar")
plt.title("RIA ARUN - 19BCE2440 -- PLOT OF DEATHS AND CURES")
plt.xlabel("Date")
plt.ylabel("No of people ")
z2 = pd.DataFrame()
z2["Date"]=(y[y["State"]=="Delhi"]["Date"])
z2["Cured_Delhi"]=(y[y["State"]=="Delhi"]["Cured"])
z2["Deaths_Delhi"]=(y[y["State"]=="Delhi"]["Deaths"])

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
table2 = ax.table(cellText=z2.values, colLabels=z2.columns, loc='center')

print(table2)
print("\nAverage is: ")
print(z2.mean(axis=0))
print("\nVariance is: ")
print(z2.var())
print("\nCorrelation is: ")
print(z2.corr(method ='pearson'))

z2.reset_index().plot(x="Date", y=["Cured_Delhi"], kind="bar")
plt.title("RIA ARUN - 19BCE2440 -- PLOT OF CURES")
plt.xlabel("Date")
plt.ylabel("No of people cured")
z2.reset_index().plot(x="Date", y=["Deaths_Delhi"], kind="bar")
plt.title("RIA ARUN - 19BCE2440 -- PLOT OF DEATHS ")
plt.xlabel("Date")
plt.ylabel("No of deaths")
z2.reset_index().plot(x="Date", y=["Cured_Delhi","Deaths_Delhi"], kind="bar")

plt.title("RIA ARUN - 19BCE2440 -- PLOT OF DEATHS AND CURES")
plt.xlabel("Date")
plt.ylabel("No of people ")
z3 = pd.DataFrame()
z3["Date"]=(y[y["State"]=="Gujarat"]["Date"])
z3["Cured_Gujarat"]=(y[y["State"]=="Gujarat"]["Cured"])
z3["Deaths_Gujarat"]=(y[y["State"]=="Gujarat"]["Deaths"])
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
table3 = ax.table(cellText=z3.values, colLabels=z3.columns, loc='center')

print(table3)
print("\nAverage is: ")
print(z3.mean(axis=0))
print("\nVariance is: ")
print(z3.var())
print("\nCorrelation is: ")
print(z3.corr(method ='pearson'))
z3.reset_index().plot(x="Date", y=["Cured_Gujarat"], kind="bar")

plt.title("RIA ARUN - 19BCE2440 -- PLOT OF CURES")
plt.xlabel("Date")
plt.ylabel("No of people cured")
z3.reset_index().plot(x="Date", y=["Deaths_Gujarat"], kind="bar")
plt.title("RIA ARUN - 19BCE2440 -- PLOT OF DEATHS ")
plt.xlabel("Date")
plt.ylabel("No of deaths")
z3.reset_index().plot(x="Date", y=["Cured_Gujarat","Deaths_Gujarat"], kind="bar")
plt.title("RIA ARUN - 19BCE2440 -- PLOT OF DEATHS AND CURES")
plt.xlabel("Date")
plt.ylabel("No of people")
