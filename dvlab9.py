# Code 1
import pandas as pd 
import matplotlib 
matplotlib.use("TkAgg") 
import matplotlib.pyplot as plt 

df = pd.read_csv("../LAB5/customer_sales.csv") 
profitList = df['total_profits'].tolist() 
monthList = df['month_number'].tolist() 
plt.plot(monthList, profitList, label='Month-wise Profit data of last year') 
plt.xlabel('Month number') 
plt.ylabel('Profit in dollar') 
plt.xticks(monthList) 
plt.title('Company profit per month') 
plt.yticks([100000, 200000, 300000, 400000, 500000]) 
plt.show()


# Code 2
import pandas as pd 
import matplotlib 
matplotlib.use("TkAgg") 
import matplotlib.pyplot as plt 
df = pd.read_csv("../LAB5/customer_sales.csv") 
monthList = df ['month_number'].tolist() 
faceCremSalesData = df ['facecream'].tolist() 
faceWashSalesData = df ['facewash'].tolist() 
toothPasteSalesData = df ['toothpaste'].tolist() 
bathingsoapSalesData = df ['bathingsoap'].tolist() 
shampooSalesData = df ['shampoo'].tolist() 
moisturizerSalesData = df ['moisturizer'].tolist() 

plt.plot(monthList, faceCremSalesData, label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', marker='o', linewidth=3) 
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3) 
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3) 
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3) 
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3) 

plt.xlabel('Month Number') 
plt.ylabel('Sales units in number') 
plt.legend(loc='upper left') 
plt.xticks(monthList) 
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000]) 
plt.title('Sales data') 
plt.show() 


# Code 3
import pandas as pd 
import matplotlib 
matplotlib.use("TkAgg") 
import matplotlib.pyplot as plt 

df = pd.read_csv("../LAB5/customer_sales.csv") 
monthList = df ['month_number'].tolist() 
faceCremSalesData = df ['facecream'].tolist() 
faceWashSalesData = df ['facewash'].tolist() 
toothPasteSalesData = df ['toothpaste'].tolist() 
bathingsoapSalesData = df ['bathingsoap'].tolist() 
shampooSalesData = df ['shampoo'].tolist() 
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot([],[],color='m', label='face Cream', linewidth=5) 
plt.plot([],[],color='c', label='Face wash', linewidth=5) 
plt.plot([],[],color='r', label='Tooth paste', linewidth=5) 
plt.plot([],[],color='k', label='Bathing soap', linewidth=5) 
plt.plot([],[],color='g', label='Shampoo', linewidth=5) 
plt.plot([],[],color='y', label='Moisturizer', linewidth=5) 
plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData, bathingsoapSalesData, shampooSalesData, moisturizerSalesData, colors=['m','c','r','k','g','y']) 
plt.xlabel('Month Number') 
plt.ylabel('Sales units in Number') 
plt.title('All product sales data using stack plot') 
plt.legend(loc='upper left') 
plt.show()
