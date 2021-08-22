# Code 1
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from google.colab import files
uploaded = files.upload()

import io
df2 = pd.read_csv(io.BytesIO(uploaded['farming.csv']))

import pandas
print('\n\t\t\t\tRIA ARUN - 19BCE2440\n')
print(df2)


# Code 2
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ccolors= ['#b4aee8','#b4aee8','#e36bae','#e36bae','#e36bae','#b4aee8']
table1 = ax.table(cellText=df2.values, colLabels=df2.columns, colColours=ccolors, loc='center')
table1.set_fontsize(28)
table1.scale(2.5, 2.5) 
plt.text(0.05, 0.12, 'RIA ARUN - 19BCE2440', style='italic', color='maroon')
print(table1)


# Code 3
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.DataFrame(data, columns = ['Name', 'Fertilizer', 'Nitrogen', 'Phosphorus', 'Potassium', 'Yield'])
fig = plt.figure()
ax = fig.add_subplot(111) 
width = 0.4
df.Yield.plot(kind='bar', color='orange', ax=ax, width=width, position=1)
plt.text(0.1, 115, 'RIA ARUN - 19BCE2440', style='italic', color='maroon')
plt.title("Bar Chart")
ax.set_ylabel('Yield')
ax.set_xlabel('Crop Number')
plt.legend();
plt.show()


# Code 4
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame(data, columns = ['Name', 'Fertilizer', 'Nitrogen', 'Phosphorus', 'Potassium', 'Yield'])
plt.text(0.85, 20, 'RIA ARUN - 19BCE2440', style='italic', color='maroon') 
plt.title("Box Plot - Nitrogen")
plt.boxplot(df['Nitrogen'])
plt.show()


# Code 5
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame(data, columns = ['Name', 'Fertilizer', 'Nitrogen', 'Phosphorus', 'Potassium', 'Yield'])
plt.text(0.85, 20, 'RIA ARUN - 19BCE2440', style='italic', color='maroon') 
plt.title("Box Plot - Potassium")
plt.boxplot(df['Potassium'])
plt.show()


# Code 6
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame(data, columns = ['Name', 'Fertilizer', 'Nitrogen', 'Phosphorus', 'Potassium', 'Yield'])
plt.text(0.85, 20, 'RIA ARUN - 19BCE2440', style='italic', color='maroon') 
plt.title("Box Plot - Phosphorus")
plt.boxplot(df['Phosphorus'])
plt.show()
