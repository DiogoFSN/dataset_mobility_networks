import os
import igraph as ig
import matplotlib.pyplot as plt
from net_metrics import net_metrics
import numpy as np
import pandas as pd

mydir = os.getcwd()
files = os.listdir(mydir + '\\IBGE_2016_mobilidade\\main_code\\input_data\\networks')
#files.remove('.DS_Store')


for file in files:
    # reading the network from file
    g = ig.Graph.Read_GraphML(mydir + '\\IBGE_2016_mobilidade\\main_code\\input_data\\networks\\' + file)

    ## minimum and maximum elements of coordinates
    min_x = np.min(g.vs["LONG"])
    max_x = np.max(g.vs["LONG"])
    min_y = np.min(g.vs["LATI"])
    max_y = np.max(g.vs["LATI"])

    dim_x = max_x - min_x
    dim_y = max_y - min_y
    scale = 20.0
    width = dim_x * scale
    height = dim_y * scale
    width = height = 1000

    ## metrics to be measured
    metrics = ['degree', 'betweenness', 'strength', 'betweenness_weight',
               'closeness_weight']  # , 'vulnerability_weight'

    ## number of nodes
    g.vcount()

    ## number of edges
    g.ecount()

    ## metrics folders
    relative_path_in = mydir + '\\IBGE_2016_mobilidade\\main_code\\results\\metrics\\' + file[:-8] + '\\in\\'
    relative_path_out = mydir + '\\IBGE_2016_mobilidade\\main_code\\results\\metrics\\' + file[:-8] + '\\out\\'
    relative_path_time = mydir + '\\IBGE_2016_mobilidade\\main_code\\results\\metrics\\' + file[:-8] + '\\time\\'
    relative_path_cost = mydir + '\\IBGE_2016_mobilidade\\main_code\\results\\metrics\\' + file[:-8] + '\\cost\\'

    ## function to generate the metrics
    net_metrics(relative_path_in, 'in', file)
    net_metrics(relative_path_out, 'out', file)
    net_metrics(relative_path_time, 'all', file, 'time')
    net_metrics(relative_path_cost, 'all', file, 'cost')

    entrada = ['in', 'out', 'time', 'cost']
    for j in entrada:
        for metric in metrics:
            # Metrics
            print('linha 56')
            df = pd.read_csv(mydir + '\\IBGE_2016_mobilidade\\main_code\\results\\metrics\\' + file[:-8] + '\\' + j + '\\' + metric + '.csv', delimiter=';',
                             header=None, encoding="latin1")
            df.columns = ['id', 'city_code', 'metric']
            print(df['metric'])

            g.vs[metric] = df['metric']
            g.vs["size"] = 12

            layout = []
            for i in range(g.vcount()):
                layout.append((g.vs[i]["LONG"], -g.vs[i]["LATI"]))

            # Ajustar para qual variavel?
            # if(g.vs[i]["label"] != "Wuhan"):
            # 	g.vs[i]["vertex_shape"] = "circle"
            # else:
            # 	g.vs[i]["vertex_shape"] = "triangle"

            g.vs['metric_plt'] = ig.rescale(g.vs[metric], clamp=True)
            cmap1 = plt.get_cmap('RdYlGn_r')
            g.vs["color"] = [cmap1(m) for m in g.vs['metric_plt']]

            if j == 'time':
                g.es['weight_plt'] = ig.rescale(g.es['MINTIME'], clamp=True)
                g.es['weight_plt'] = ig.rescale(g.es['MINTIME'], (0.005, 0.05))
            elif j == 'cost':
                g.es['weight_plt'] = ig.rescale(g.es['MINCOST'], clamp=True)
                g.es['weight_plt'] = ig.rescale(g.es['MINCOST'], (0.005, 0.05))
            else:
                g.es['weight_plt'] = ig.rescale(g.es['weight'], clamp=True)
                g.es['weight_plt'] = ig.rescale(g.es['weight'], (0.005, 0.11))

            cmap2 = plt.get_cmap('RdYlGn_r')
            g.es["color"] = [cmap2(w) for w in g.es['weight_plt']]

            g.es["edge_width"] = [w ** 1.5 * 150 for w in g.es['weight_plt']]

            visual_style = {
                "vertex_size": g.vs["size"],
                # "vertex_shape": eG.vs["vertex_shape"],
                "vertex_label_size": 20,
                "vertex_label_dist": 1,
                "vertex_label_color": "white",
                "edge_width": g.es['edge_width'],
                "layout": layout,
                "bbox": (width, height),
                "margin": 30,
                "edge_arrow_size": 0.2
            }

            ig.plot(g, mydir + '\\IBGE_2016_mobilidade\\main_code\\results\\metrics\\' + file[:-8] + '\\' + j + '\\' + metric + '.png', **visual_style)
