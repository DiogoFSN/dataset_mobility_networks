import os
import igraph as ig
import pandas as pd
import numpy

mydir = os.getcwd()
path_xlsx = mydir + "\\br_sao_paulo_mobility_network_by_subway_in_2017\\network_non_motorized_mode_trips\\raw_data\\Non_motorized_mode_trips.xlsx"
atributos = mydir + "\\br_sao_paulo_mobility_network_by_subway_in_2017\\network_non_motorized_mode_trips\\raw_data\\centroides_zonasSP.csv"

# Load data from file xlsx and csv
data = pd.read_excel(path_xlsx, header= 0, index_col=0)
drop_indices = numpy.arange(343,len(data)+1)

#Column
data = data.drop(drop_indices, axis=1)

#Line
data = data.drop(drop_indices)
atrib = pd.read_csv(atributos, delimiter = ';')

# Create the graph 
flow_matrix = data.to_numpy()
g = ig.Graph.Weighted_Adjacency(flow_matrix.tolist(), attr="weight", mode="directed") 

# Insert attributes at vertices
for i, row in atrib.iterrows():
    g.vs[i]['NumeroZona'] = row['NumeroZona']
    g.vs[i]['NomeZona'] = row['NomeZona']
    g.vs[i]['NumeroMuni'] = row['NumeroMuni']
    g.vs[i]['NomeMunici'] = row['NomeMunici']
    g.vs[i]['NumDistrit'] = row['NumDistrit']
    g.vs[i]['Area_ha_2'] = row['Area_ha_2']
    g.vs[i]['COORD_X'] = row['COORD_X']
    g.vs[i]['COORD_Y'] = row['COORD_Y']
    
# Save the graph in format GraphML
g.write_graphml(mydir + "\\br_sao_paulo_mobility_network_by_subway_in_2017\\network_non_motorized_mode_trips\\networks\\Graph_Non_motorized_mode_trips.GraphML")


