import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 

import random as random 
from matplotlib.lines import Line2D 

%matplotlib inline 

serial_number = [I for I in range(1,21)] 
cgpa = [6,6.5,7,8,9,6,7.5,6.5,8,9,9.5,7,6.5,4,8,10,7.9,8.6,9,6.8] 
program =['CSE', 'CSE', 'ECE', 'ECE', 'EEE', 'CSE', 'CSE', 'CSE', 'EEE', 'ECE', 'ECE', 'EEE', 'CSE', 'CSE', 'EEE', 'CSE', 'ECE', 'ECE', 'CSE', 'EEE'] 
gender =['F','M','F','M','F','F','M','M','M','M','M','F','M','M','F','M','M','M','F','M'] 

df = pd.DataFrame({'Serial Number':serial_number,'CGPA': cgpa,'Btech Program': program,'Gender': gender}) 
df.set_index('Serial Number', inplace=True) 

fig, ax = plt.subplots(figsize=(12, 9)) 
program_colours = {'CSE': '#006400', 'ECE':'#8B0000', 'EEE':'#00008b'} gender_marker={'M': 'o', 'F':'x'} 
for kind in gender_marker: df = df[df.Gender == kind] ax.scatter(df.index.tolist(),df['CGPA'],
marker = gender_marker[kind], s = 150, linewidth = 2, c = df['Btech Program'].apply(lambda y: program_colours[y])) 

program_lines = [Line2D([0], [0], color= '#006400', lw=5), Line2D([0], [0], color= '#8B0000', lw=5),Line2D([0], [0], color= '#00008b', lw=5)]
 gender_lines = [Line2D([0], [0], marker= 'o', color = '#111111'),Line2D([0], [0], marker= 'x', color = '#111111')] 

legend_1 = ax.legend(program_lines, ['CSE', 'ECE', 'EEE'], loc ='lower right', fontsize = 20) legend_2 = ax.legend(gender_lines, ['Male', 'Female'], loc ='lower left', fontsize = 20) ax.add_artist(legend_1) 

plt.ylabel('CGPA', fontsize = 15) 
plt.xlabel('Serial Number', fontsize = 15) 
plt.title('ScatterPlot - Grades Vs Serial Number with B.Tech Program and Gender Channels', fontsize=15) 

plt.xticks(np.arange(1, 21, 1)) 
plt.plot()
