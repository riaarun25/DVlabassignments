#Scatter plot for Age of People

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import csv
df= pd.read_csv("../Lab3/persinf.csv")
x = df['person']
y = df['age']
t = np.arange(20)
plt.scatter(x, y, c=t)
plt.title("Age of people")
plt.xlabel("People")
plt.ylabel("Age")
plt.show()


#Scatter plot for Height of People

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import csv
df= pd.read_csv("../Lab3/persinf.csv")
x = df['person']
y = df['height']
t = np.arange(20)
plt.scatter(x, y, c=t)
plt.title("Height of people")
plt.xlabel("People")
plt.ylabel("Height")
plt.show()


#Scatter plot with colormap on Age of People

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import csv
df= pd.read_csv("../Lab3/persinf.csv")
x = df['person']
y = df['age']
t = np.arange(20)
plt.scatter(x, y, c=t, cmap='inferno')
plt.colorbar()
plt.title("Age of people")
plt.xlabel("People")
plt.ylabel("Age")
plt.show()


#Scatter plot with colormap on Height of People

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import csv
df= pd.read_csv("../Lab3/persinf.csv")
x = df['person']
y = df['height']
t = np.arange(20)
plt.scatter(x, y, c=t, cmap='inferno')
plt.colorbar()
plt.title("Height of people")
plt.xlabel("People")
plt.ylabel("Height")
plt.show()


    ##########


#Colorplot of COVID-19 caes on the Indian Map
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import geopandas as gpd
import geoplot
from mpl_toolkits.axes_grid1 import make_axes_locatable
fp = "/india_administrative_state_boundary.shp"
gdf = gpd.read_file(fp)
gdf.head()df = pd.read_csv("/covid_19_india.csv", header=0)
df.head()
df=df[['sno','Date','Region','Confirmed Cases','Active Cases','Cured/Discharged','Death']]
dataframemerged = pd.merge(gdf, df, left_on="gid", right_on= "sno")
dataframemerged.head()
ax = plt.subplot(aspect='equal')
vmin, vmax = -1, 1
dataframemerged.plot(column= 'Confirmed Cases' ,cmap='ocean', scheme='quantiles', 
ax=ax)
fig = ax.get_figure()
cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
sm = plt.cm.ScalarMappable(cmap='ocean', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
fig.colorbar(sm, cax=cax)
