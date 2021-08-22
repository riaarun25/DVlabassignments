# Code 1
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

from google.colab import files
uploaded = files.upload()

import io
df2 = pd.read_csv(io.BytesIO(uploaded['assignment2.csv']))

import pandas
print(df2)


# Code 2
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

ccolors= ['#008891','#75cfb8','#75cfb8','#75cfb8','#75cfb8','#75cfb8','#008891','#75cfb8','#75cfb8']
table1 = ax.table(cellText=df2.values, colLabels=df2.columns, colColours=ccolors, loc='center')

table1.set_fontsize(28)
table1.scale(2.5, 2.5) 
plt.text(0.05, 0.395, 'RIA ARUN - 19BCE2440', style='italic', color='maroon')
print(table1)


# Code 3
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
colors =[['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], 
         ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3'], ['#a7c5eb','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#c1a1d3','#a7c5eb','#c1a1d3','#c1a1d3']]
table1 = ax.table(cellText=df2.values, colLabels=df2.columns, cellColours=colors, loc='center')
table1.set_fontsize(28)
table1.scale(2.5, 2.5) 
plt.text(0.05, 0.395, 'RIA ARUN - 19BCE2440', style='italic', color='maroon')
print(table1)


# Code 4
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
table=ax.table(cellText=df2.values, colLabels=df2.columns, cellColours=colors, loc='center')
table.set_fontsize(28)
table.scale(2.5, 2.5)

for i in range(51):
  table.get_celld()[(i,0)].set_facecolor('#c6a9a3')

for i in range(51):
  table.get_celld()[(i,1)].set_facecolor('#b34180')

for i in range(51):
  table.get_celld()[(i,2)].set_facecolor('#b34180')

for i in range(51):
  table.get_celld()[(i,3)].set_facecolor('#c6a9a3')

for i in range(51):
  table.get_celld()[(i,4)].set_facecolor('#b34180')

for i in range(51):
  table.get_celld()[(i,5)].set_facecolor('#c6a9a3')

for i in range(51):
  table.get_celld()[(i,6)].set_facecolor('#c6a9a3')

for i in range(51):
  table.get_celld()[(i,7)].set_facecolor('#c6a9a3')

for i in range(51):
  table.get_celld()[(i,8)].set_facecolor('#c6a9a3')


# Code 5
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
table=ax.table(cellText=df2.values, colLabels=df2.columns, loc='center')
table.set_fontsize(28)
table.scale(2.5, 2.5)

for i in range(51):
  table.get_celld()[(i,0)].set_edgecolor('#e27802')

for i in range(51):
  table.get_celld()[(i,1)].set_edgecolor('#008891')

for i in range(51):
  table.get_celld()[(i,2)].set_edgecolor('#008891')

for i in range(51):
  table.get_celld()[(i,3)].set_edgecolor('#e27802')

for i in range(51):
  table.get_celld()[(i,4)].set_edgecolor('#008891')

for i in range(51):
  table.get_celld()[(i,5)].set_edgecolor('#e27802')

for i in range(51):
  table.get_celld()[(i,6)].set_edgecolor('#e27802')

for i in range(51):
  table.get_celld()[(i,7)].set_edgecolor('#e27802')

for i in range(51):
  table.get_celld()[(i,8)].set_edgecolor('#e27802')
