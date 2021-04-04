# line plot using the columns empid, sales, income
import pandas as pd 
import matplotlib.pyplot as plt 

data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40]] 

df = pd.DataFrame(data, columns = ['EMPID', 'Gender','Age', 'Sales','BMI', 'Income'])
plt.text(3, 440, 'RIA ARUN - 19BCE2440', style='italic', color='maroon')
plt.title("Line Plot")
plt.xlabel("EMPID")
plt.ylabel("Value")
plt.plot(df["EMPID"],df["Income"], linewidth=1)
plt.plot(df["EMPID"], df["Income"], color='b', marker='x', label='Income')
plt.plot(df["EMPID"],df["Sales"], linewidth=1)
plt.plot(df["EMPID"], df["Sales"], color='c', marker='x', label='Sales')
plt.legend();
plt.show()



# bar plot empid, sales, income
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 
df = pd.DataFrame(data, columns = ['EMPID', 'Gender', 'Age', 'Sales', 'BMI', 'Income'])

fig = plt.figure()
ax = fig.add_subplot(111) 
ax2 = ax.twinx()
width = 0.3
df.Income.plot(kind='bar', color='orange', ax=ax, width=width, position=1)
df.Sales.plot(kind='bar', color='green', ax=ax2, width=width, position=0)
plt.text(3, 140, 'RIA ARUN - 19BCE2440', style='italic', color='maroon')
plt.title("Bar Chart")
ax.set_ylabel('Income')
ax2.set_ylabel('Sales')
ax.set_xlabel('EMPID')
plt.legend();
plt.show()



# histogram gender, BMI
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 

df = pd.DataFrame(data, columns = ['EMPID', 'Gender', 'Age', 'Sales', 'BMI', 'Income'] ) 
fig = plt.figure()
ax = fig.add_subplot(111)
plt.text(1.5, 6, 'RIA ARUN - 19BCE2440', style='italic', color='maroon')
plt.hist(df['Gender'], bins=3, facecolor='grey')
plt.hist(df['BMI'], bins=10, facecolor='blue', alpha=0.3)
plt.title('Histogram - Gender and BMI')
plt.ylabel('EMPID')
plt.show()



# boxplot for income
import pandas as pd 
import matplotlib.pyplot as plt 

data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 
df = pd.DataFrame(data, columns = ['EMPID', 'Gender', 'Age', 'Sales', 'BMI', 'Income'] )
plt.text(0.85, 410, 'RIA ARUN - 19BCE2440', style='italic', color='maroon') 
plt.title("Box Plot")
plt.boxplot(df['Income'])
plt.show()

