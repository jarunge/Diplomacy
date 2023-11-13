'''
Using graph theory on a diplomacy map
This script  is the basic one from chat GPT. Edit as needed
'''

import networkx as nx
import matplotlib.pyplot as plt
import sys
import base_map as bm

########################################################################
#################    Territories    ####################################
########################################################################
land_territories = bm.land_territoies
sea_territories = bm.sea_territories


fleet_spaces = sea_territories + bm.coastal_land
#############################################################################
################   Connections between Territories     ######################
#############################################################################

# Connections between supply centers
land_connections = bm.land_connections
coastal_connections = bm.coastal_connections
sea_connections = bm.sea_connections

##############################################################################
##############################################################################

# # Create a directed graph- connections are (source, target) pairs
# diplomacy_map = nx.DiGraph()

# Create an undirected graph
diplomacy_map = nx.Graph()

# Add territories as nodes
territories = land_territories + sea_territories
diplomacy_map.add_nodes_from(territories)

# Define the borders or adjacency relationships between territories
borders =  land_connections + coastal_connections + sea_connections

# Add edges to the graph
diplomacy_map.add_edges_from(borders)
##############################################################################
#############  The graph is now created.  You can add attributes   ###########
#############     to the nodes and edges                           ###########
##############################################################################
## Home centers - can build
home_centers = bm.home_centers

# Add attributes to the nodes
for node in diplomacy_map.nodes:
    diplomacy_map.nodes[node]['home_center'] = 'none'
    ## Assign supply center
    if node in supply_centers:
        diplomacy_map.nodes[node]['supply_center'] = True
    else:
        diplomacy_map.nodes[node]['supply_center'] = False
    ## Assign domain
    if node in Land_territories:
        diplomacy_map.nodes[node]['domain'] = 'land'
        diplomacy_map.nodes[node]['army'] = True
        if node in coastal_land:
            diplomacy_map.nodes[node]['fleet'] = True
        else:
            diplomacy_map.nodes[node]['fleet'] = False
    elif node in sea_territories:
        diplomacy_map.nodes[node]['domain'] = 'sea'
        diplomacy_map.nodes[node]['army'] = False
        diplomacy_map.nodes[node]['fleet'] = True
    else:
        print(f"Error: {node} is not in Land_territories, or sea_territories")
        sys.exit()
    
## Assign home centers
for player, centers in home_centers.items():
    for center in centers:
        diplomacy_map.nodes[center]['home_center'] = player

#############################################################################
############       Draw the graph          ##################################
#############################################################################
pos = nx.spring_layout(diplomacy_map, seed=42)  # You can choose a different layout if needed
nx.draw(diplomacy_map, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='lightblue', font_size=6, edge_color='gray')

# Show the graph
plt.show()

##############################################################################
#############  Now you can use the graph to find shortest paths   ############
#############  and other graph theory applications                 ############
##############################################################################

# Example: Find the distance between 'London' and 'Paris'
start_territory = 'London'
end_territory = 'Paris'

# Use shortest_path_length to find the distance
distance = nx.shortest_path_length(diplomacy_map, source=start_territory, target=end_territory)





