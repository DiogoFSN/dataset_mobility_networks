import os
import igraph as ig
import numpy as np
import vulnerability as vn
from pathlib import Path

mydir = os.getcwd()


def net_metrics(relative_path, mode, file, opt=''):
    # in_or_out = 'in' if 'in' in mode else 'out'

    # create directory if it does not exist
    Path(relative_path).mkdir(parents=True, exist_ok=True)

    ## function to export data .csv
    def export_data(g, data, stat):
        # Saving results to file
        file_out = open(relative_path + stat + '.csv', 'w')
        for i in range(g.vcount()):
            file_out.write(str(g.vs[i]['NOMEMUN']) + ';' + str(int(g.vs[i]['geocode'])) + ';' + str(data[i]) + '\n')
        file_out.close()

    ## function calculates heterogeneity
    def heterogeneity(g):
        degrees = g.degree(mode=mode)
        acc = 0
        for k in degrees:
            acc = acc + k ** 2
        avg = acc / len(degrees)
        het = avg / (np.mean(degrees) ** 2)
        return het

    # reading the network from file
    g = ig.Graph.Read_GraphML(mydir + '\\road_and_waterway_connections_IBGE_2016\\input_data\\networks\\' + file)
    # g.to_undirected()

    print('  Density  ')
    density = g.density()
    file_out = open(relative_path + 'density.csv', 'w')
    file_out.write(str(density))
    file_out.close()

    print('  Kappa  ')
    kappa = heterogeneity(g)
    file_out = open(relative_path + 'kappa.csv', 'w')
    file_out.write(str(kappa))
    file_out.close()

    ########## UNWEIGHTED ##########
    print('  Degree ')
    degrees = g.degree(mode=mode)
    export_data(g, degrees, 'degree')

    print('  Betweenness  ')
    betweenness = g.betweenness(vertices=None, directed=True, cutoff=None)
    export_data(g, betweenness, 'betweenness')

    print('  Closeness  ')
    closeness = g.closeness(vertices=None, mode=mode, cutoff=None, weights=None, normalized=True)
    export_data(g, closeness, 'closeness')

    # print('  Vulnerability  ')
    # vuln = vn.vulnerability(g, weights=None, mode=mode)
    # export_data(g, vuln, 'vulnerability')

    ########## WEIGHTED ##########

    # strength (flows are the weights)
    if opt == '':
        print('  Strength ')
        strength = g.strength(weights='weight', mode=mode)
        export_data(g, strength, 'strength')

        # Inverse of the flow
        # This is a valid notion of distance in mobility networks,
        # since the higher the flows between neighbors, the closer they are.
        g.es['w_inv'] = 1.0 / np.array(g.es['weight'])
    elif opt == 'time':
        print('  Strength ')
        strength = g.strength(weights='MINTIME', mode=mode)
        export_data(g, strength, 'strength')

        # Inverse of the flow
        # This is a valid notion of distance in mobility networks,
        # since the higher the flows between neighbors, the closer they are.
        max = np.max(g.es['MINTIME'])
        g.es['w_inv'] = np.array(g.es['MINTIME']) / max
    elif opt == 'cost':
        print('  Strength ')
        strength = g.strength(weights='MINCOST', mode=mode)
        export_data(g, strength, 'strength')

        # Inverse of the flow
        # This is a valid notion of distance in mobility networks,
        # since the higher the flows between neighbors, the closer they are.
        g.es['w_inv'] = 1.0 / np.array(g.es['MINCOST'])

    print('  Diameter ')
    diameter = g.diameter(directed=True, weights='w_inv')
    file_out = open(relative_path + 'diameter.csv', 'w')
    file_out.write(str(diameter))
    file_out.close()

    print('  Weighted Betweenness ')
    betweenness_w = g.betweenness(vertices=None, directed=True, cutoff=None, weights='w_inv')
    export_data(g, betweenness_w, 'betweenness_weight')

    print('  Weighted Closeness ')
    closeness_w = g.closeness(vertices=None, mode=mode, cutoff=None, weights='w_inv', normalized=True)
    export_data(g, closeness_w, 'closeness_weight')

    # print('  Weighted Vulnerability ')
    # vuln_w = vn.vulnerability(g, weights='w_inv', mode=mode)
    # export_data(g, vuln_w, 'vulnerability_weight')