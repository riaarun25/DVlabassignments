source_node_id = [0,0,0,1,1,1,2,2,469,469,469,6,6,385,385,385,3,3,3,3,4,4] destination_node_id = [1,2,469,0,6,385,0,3,0,380,374,1,5,1,384,386,2,4,419,422,3,5] distance = [5,10,56,5,78,500,10,35,78,45,68,78,134,45,56,50,35,90,89,78,90,100] 
safety = [0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1]

df = pd.DataFrame({ 
'Source Node ID' : source_node_id, 
'Destination Node ID': destination_node_id, 
'Distance' : distance, 
'Safety':safety}) 
G = nx.from_pandas_edgelist(df, 
source='Source Node ID', 
target='Destination Node ID', 
edge_attr='Distance')
edges = G.edges() 

edge_color_list = [] 
edge_width_list = [] 
for i, j in edges: 
   if G.edges[i,j]['Distance'] <= 50: 
   edge_color_list.append('green')
   edge_width_list.append(4) 
elif (G.edges[i,j]['Distance'] > 50) and (G.edges[i,j]['Distance'] <= 100):
   edge_color_list.append('blue') 
   edge_width_list.append(6) 
elif G.edges[i,j]['Distance'] > 100: 
   edge_color_list.append('red') 
   edge_width_list.append(8) 

for i, j, k in zip(df['Source Node ID'], df['Destination Node ID'], df['Safety']): G.edges[i,j]['Safety'] = k 

edge_safety_list = []
for i, j in edges: 
  if G.edges[i,j]['Safety'] == 0: 
    edge_safety_list.append('--') 
  elif G.edges[i,j]['Safety'] == 1: 
   edge_safety_list.append('-') 

fig, ax = plt.subplots(figsize=(12,10)) 
nx.draw(G, edge_color=edge_color_list, width=edge_width_list, with_labels=True, style=edge_safet y_list)

ax.axis('off') 
ax.set_title('Node-Edge Diagram', fontdict={'fontsize':'20','fontweight':'3'}) 
xycoords='figure fraction', horizontalalignment='left', 
verticalalignment='top', fontsize=12, color='#555555')
edge_color_lines = [Line2D([0], [0], color='green', lw=4), 
Line2D([0], [0], color='blue', lw=4), 
Line2D([0], [0], color= 'red', lw=4)] 
safety_lines = [Line2D([0], [0], color='#000000', lw=4),
Line2D([0], [0], color='#000000', lw=4)] 

legend_1 = ax.legend(edge_color_lines, ['Distance < 50', 'Distance < 100 and > 50', 'Distance > 100']) 
legend_2 = ax.legend(presence_lines, ['Dotted Lines = Safety - 0', 'Solid Lines = Safety - 1'], loc='uppe r left') ax.add_artist(legend_1) plt.show()
