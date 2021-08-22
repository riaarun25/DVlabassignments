import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
import random as random 
import geopandas as gpd 

from splot.mapping import vba_choropleth 
from matplotlib.lines import Line2D 

dataframe = gpd.read_file('/content/india_administrative_state_boundary.shp') 

animals = ['Elephant', 'Lion', 'Tiger'] 
presence = [0,1] 
animals_list = [] 

presence_list = [] 
for _ in range(len(dataframe)): 
  animals_list.append(random.choice(animals)) 
  presence_list.append(random.choice(presence)) 

dataframe['Animal'] = animals_list 
dataframe['Presence'] = presence_list 
dataframe['Animal'] = dataframe['Animal'].replace(['Elephant', 'Tiger', 'Lion'], [1,2,3]) 
fig, ax = plt.subplots(figsize=(12,10))
color_list = ['#a1dab4','#41b6c4','#225ea8'] 

vba_choropleth( 
dataframe['Animal'].values, 
dataframe['Presence'].values, 
dataframe, 
rgb_mapclassify=dict(classifier='quantiles'), 
alpha_mapclassify=dict(classifier='quantiles'), 
cmap=color_list, 
ax=ax, 
revert_alpha=False, 
legend=True 
) 

ax.axis('off') 
ax.set_title('Animals and Their Presence in the Indian States', 
fontdict={'fontsize': '20', 'fontweight': '3'}) 
ax.annotate(RIA ARUN | 19BCE2440', xy=(0.1, .08), 
xycoords='figure fraction', horizontalalignment='left', 
verticalalignment='top', fontsize=12, color='#555555') 
animal_lines = [Line2D([0], [0], color='#a1dab4', lw=4), 
Line2D([0], [0], color='#41b6c4', lw=4), 
Line2D([0], [0], color='#225ea8', lw=4)] 
presence_lines = [Line2D([0], [0], color='#ffffff', lw=4), 
Line2D([0], [0], color='#111111', lw=4)] 

legend_1 = ax.legend(animal_lines, ['Elephant', 'Tiger', 'Lion']) 
legend_2 = ax.legend(presence_lines, ['Not Present - 0', 'Present - 1'], loc='upper left') ax.add_artist(legend_1)
