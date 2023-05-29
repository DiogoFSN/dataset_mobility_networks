import os
import igraph as ig
import numpy as np
import pandas as pd

mydir = os.getcwd()
files = os.listdir(mydir + '\\saopaulo_mobility_network\\network_Bike_trips\\networks\\')

# Load the graph from the GraphML file
for file in files:
    # Reading the network from file
    g = ig.Graph.Read_GraphML(mydir + '\\saopaulo_mobility_network\\network_Bike_trips\\networks\\' + file)

    # Minimum and maximum elements of coordinates
    min_x = np.min(g.vs["COORD_X"]) 
    max_x = np.max(g.vs["COORD_X"])
    min_y = np.min(g.vs["COORD_Y"])
    max_y = np.max(g.vs["COORD_Y"])

    dim_x = max_x - min_x
    dim_y = max_y - min_y
    scale = 20.0
    width = dim_x * scale
    height = dim_y * scale
    width = height = 1000

    layout = []
    for i in range(g.vcount()):
        layout.append((g.vs[i]["COORD_X"], -g.vs[i]["COORD_Y"]))
    
    visual_style = {
        "vertex_label_size": 20,
        "vertex_label_dist": 1,
        "vertex_label_color": "white",
        "layout": layout,
        "bbox": (width, height),
        "margin": 30,
        "edge_arrow_size": 0.2
    }

    ig.plot(g, mydir + '\\saopaulo_mobility_network\\network_Bike_trips\\results\\'+ file + 'Graph_Bike_trips.png' , **visual_style)

        
