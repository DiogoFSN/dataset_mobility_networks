import os
import igraph as ig
import numpy as np
from pathlib import Path
import pandas as pd

mydir = os.getcwd()
files = os.listdir(mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\input_data\\networks')
files.sort(reverse=True)
#files.remove('.DS_Store')

for file in files:
    # reading the network from file
    g = ig.Graph.Read_GraphML(mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\input_data\\networks\\' + file)

    ## Elementos minimos e maximos das coordenadas
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

    ## Detalhes da rede
    g.summary()

    ## Numero de nós
    g.vcount()

    ## Numero de arestas
    g.ecount()

    ## Atributos dos nós
    g.vertex_attributes()

    ## Atributos das arestas
    g.edge_attributes()

    ## Pastas das metricas
    relative_path = mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\results\\clusters\\' + file[:-8]

    entrada = ['in', 'out', 'time', 'cost']

    # df = pd.DataFrame(columns=[files, entrada], index=['Modularidade Infomap', 'Modularidade Walktrap'])

    for j in entrada:
        g.vs["size"] = 12

        layout = []
        for i in range(g.vcount()):
            layout.append((g.vs[i]["LONG"], -g.vs[i]["LATI"]))

        if j == 'time':
            g.es['weight_plt'] = ig.rescale(g.es['MINTIME'], clamp=True)
            g.es['weight_plt'] = ig.rescale(g.es['MINTIME'], (0.005, 0.05))
        elif j == 'cost':
            g.es['weight_plt'] = ig.rescale(g.es['MINCOST'], clamp=True)
            g.es['weight_plt'] = ig.rescale(g.es['MINCOST'], (0.005, 0.05))
        else:
            g.es['weight_plt'] = ig.rescale(g.es['weight'], clamp=True)
            g.es['weight_plt'] = ig.rescale(g.es['weight'], (0.005, 0.11))

        g.es["edge_width"] = [w ** 1.5 * 150 for w in g.es['weight_plt']]

        print(f'{file[:-8]} {j}')

        if j == 'time':
            infomap = g.community_infomap(edge_weights="MINTIME")  # , vertex_weights="", trials=10
            walktrap = g.community_walktrap(weights="MINTIME", steps=1).as_clustering()
            # GirvanNewman = g.community_edge_betweenness(directed=True,
            #                                             weights="MINTIME").as_clustering()  # clusters=None
            # louvain = g.community_multilevel(weights="MINTIME", return_levels=True)
        elif j == 'cost':
            infomap = g.community_infomap(edge_weights="MINCOST")
            walktrap = g.community_walktrap(weights="MINCOST", steps=1).as_clustering()
            # GirvanNewman = g.community_edge_betweenness(directed=True,
            #                                             weights="MINCOST").as_clustering()
            # louvain = g.community_multilevel(weights="MINCOST", return_levels=True)
        else:
            infomap = g.community_infomap(edge_weights="weight")
            walktrap = g.community_walktrap(weights="weight", steps=1).as_clustering()
            # GirvanNewman = g.community_edge_betweenness(directed=True,
            #                                             weights="weight").as_clustering()
            # louvain = g.community_multilevel(weights="weight", return_levels=True)

        mod_info = infomap.modularity
        print(f'Modularidade Infomap {mod_info}')
        mod_walk = walktrap.modularity
        print(f'Modularidade Walktrap {mod_walk}')
        # mod_GN = GirvanNewman.modularity
        # print(f'Modularidade Girvan Newman {mod_GN}')
        # mod_Louvain = louvain.modularity
        # print(f'Modularidade Louvain {mod_Louvain}')

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

        Path(mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\results\\clusters\\' + file[:-8] + '\\' + j + '\\').mkdir(parents=True, exist_ok=True)
        ig.plot(infomap, mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\results\\clusters\\' + file[:-8] + '\\' + j + '\\' + 'infomap' + '.png', **visual_style)
        ig.plot(walktrap, mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\results\\clusters\\' + file[:-8] + '\\' + j + '\\' + 'walktrap' + '.png', **visual_style)
        # ig.plot(GirvanNewman, mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\results\\clusters\\' + file[:-8] + '\\' + j + '\\' + 'GirvanNewman' + '.png',
        #         **visual_style)
        # ig.plot(louvain, mydir + '\\IBGE_2016_mobilidade_covid-masters\\main_code\\results\\clusters\\' + file[:-8] + '\\' + j + '\\' + 'louvain' + '.png', **visual_style)
