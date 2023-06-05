import os
import igraph as ig
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

mydir = os.getcwd()
print('mydir: ', mydir)
## store file path
path_xlsx = mydir + "\\IBGE_2016_mobilidade\\main_code\\input_data\\raw_data\\Base_de_dados_ligacoes_rodoviarias_e_hidroviarias_2016.xlsx"

## create dataset from original data
data = pd.read_excel(path_xlsx, header= 0, index_col=0)

## state code (in Brazil the maximum is 53)  
data.COD_UF_A.unique()

## greater than 53 were found in B (80, 87, 92, 88, 82, 81, 91)
data.COD_UF_B.unique()

## first 5 elements
data.head()

## data type
data.dtypes

## withdrawing the lines with state code above 53
data = data[data.COD_UF_A <= 53]
data = data[data.COD_UF_B <= 53]

## remove unimportant columns
data.drop(['COD_UF_A', 'UF_A', 'COD_UF_B', 'UF_B'], axis=1, inplace=True)

## checking for null values
data.isnull().values.any()

## how many null values
data.isnull().sum().sum()

## where are the null values and their quantify
data['VAR01'].isnull().values.any()
data['VAR01'].isnull().sum()

data['VAR02'].isnull().values.any()
data['VAR02'].isnull().sum()

## filling in null spaces
data.VAR01.fillna('Missing', inplace=True)
data.VAR02.fillna('Missing', inplace=True)

## Checking if there are still null values
data.isnull().values.any()

## Converting Yes/No to Y/N
data.VAR13 = data.VAR13.astype(str).str[0]

## Transforming data from the names of municipalities (categorical) into numerical ones  
label_encoder_var01 = LabelEncoder()
data.VAR01 = label_encoder_var01.fit_transform(data.VAR01.values)

label_encoder_var02 = LabelEncoder()
data.VAR02 = label_encoder_var02.fit_transform(data.VAR02.values)

## first 5 elements
data.head()

## Saving the new dataset
data.to_excel(mydir + "\\IBGE_2016_mobilidade\\main_code\\input_data\\raw_data\\dataset_transform.xlsx", encoding="utf8")

## Loading the dataset
data = pd.read_excel(mydir + "\\IBGE_2016_mobilidade\\main_code\\input_data\\raw_data\\dataset_transform.xlsx", header=0)

## Function exists node
def has_node(graph, name):
    try:
        graph.vs.find(name=name)
    except:
        return False
    return True


## Function insert node
def add_vertex(graph, id, nome, hurb, long, lati):
    graph.add_vertex(id, geocode=id)
    graph.vs.find(geocode=id)['NOMEMUN'] = nome  # City name
    graph.vs.find(geocode=id)['HURB'] = hurb  # type of place
    graph.vs.find(geocode=id)['LONG'] = long  # Longitude
    graph.vs.find(geocode=id)['LATI'] = lati  # Latitude


## function insert edge
def add_edge(graph, opt, a, b, id, cost, time, hidro, rodo, veic):
    graph.add_edge(a, b, id=id)  # path id
    graph.es.find(id=id)['MINCOST'] = cost  # minimum cost (R$)
    graph.es.find(id=id)['MINTIME'] = time  # minimum time (min)
    if opt == 1:
        graph.es.find(id=id)['FREQHIDRO'] = hidro  # Number of trips by river
        graph.es.find(id=id)['FREQRODO'] = rodo  # Number of road trips
        graph.es.find(id=id)['FREQVEIC'] = veic  # Number of informal trips
        graph.es.find(id=id)['weight'] = hidro + rodo + veic  # Number of trips by all means
    if opt == 2:
        graph.es.find(id=id)['weight'] = hidro  # Number of trips by river
    if opt == 3:
        graph.es.find(id=id)['weight'] = rodo  # Number of trips by river
    if opt == 4:
        graph.es.find(id=id)['weight'] = hidro + rodo + veic  # Number of trips by all means


## function build the graph
def build_graph(data, directed=False):
    g1 = ig.Graph(directed=directed)  # complete graph
    g2 = ig.Graph(directed=directed)  # hydro flow graph
    g3 = ig.Graph(directed=directed)  # road flow graph
    g4 = ig.Graph(directed=directed)  # summed flow graph
    print('linha 116')
    for index, row in data.iterrows():
        # starting node
        id_1 = str(row["CODMUNDV_A"])  # county code
        # arrival node
        id_2 = str(row["CODMUNDV_B"])  # county code

        if not has_node(g1, id_1):
            # starting node g1
            add_vertex(g1, id_1, row['NOMEMUN_A'], row['VAR01'], row['VAR08'], row['VAR09'])
            # starting node g4
            add_vertex(g4, id_1, row['NOMEMUN_A'], row['VAR01'], row['VAR08'], row['VAR09'])
        if not has_node(g1, id_2):
            # arrival node g1
            add_vertex(g1, id_2, row['NOMEMUN_B'], row['VAR02'], row['VAR10'], row['VAR11'])
            # arrival node g4
            add_vertex(g4, id_2, row['NOMEMUN_B'], row['VAR02'], row['VAR10'], row['VAR11'])

        # edge g1
        add_edge(g1, 1, id_1, id_2, row['ID'], row['VAR03'], row['VAR04'], row['VAR05'], row['VAR06'], row['VAR12'])
        # edge g4
        add_edge(g4, 4, id_1, id_2, row['ID'], row['VAR03'], row['VAR04'], row['VAR05'], row['VAR06'], row['VAR12'])

        # graph Hidro
        if row['VAR05'] > 0:
            if not has_node(g2, id_1):
                # starting node g2
                add_vertex(g2, id_1, row['NOMEMUN_A'], row['VAR01'], row['VAR08'], row['VAR09'])
            if not has_node(g2, id_2):
                # arrival node g2
                add_vertex(g2, id_2, row['NOMEMUN_B'], row['VAR02'], row['VAR10'], row['VAR11'])
            # edge g2
            add_edge(g2, 2, id_1, id_2, row['ID'], row['VAR03'], row['VAR04'], row['VAR05'], row['VAR06'], row['VAR12'])
        # graph Rodo
        if row['VAR06'] > 0:
            if not has_node(g3, id_1):
                # starting node g3
                add_vertex(g3, id_1, row['NOMEMUN_A'], row['VAR01'], row['VAR08'], row['VAR09'])
            if not has_node(g3, id_2):
                # arrival node g3
                add_vertex(g3, id_2, row['NOMEMUN_B'], row['VAR02'], row['VAR10'], row['VAR11'])
            # edge g3
            add_edge(g3, 3, id_1, id_2, row['ID'], row['VAR03'], row['VAR04'], row['VAR05'], row['VAR06'], row['VAR12'])
    
    
    ## save graph
    g1.write_graphml(mydir + "\\IBGE_2016_mobilidade\\main_code\\input_data\\networks\\grafo_completo.GraphML")
    g2.write_graphml(mydir + "\\IBGE_2016_mobilidade\\main_code\\input_data\\networks\\grafo_peso_hidro.GraphML")
    g3.write_graphml(mydir + "\\IBGE_2016_mobilidade\\main_code\\input_data\\networks\\grafo_peso_rodo.GraphML")
    g4.write_graphml(mydir + "\\IBGE_2016_mobilidade\\main_code\\input_data\\networks\\grafo_peso_somado.GraphML")

    
    #return g1, g2, g3, g4

## builds the graph from the modified data
#g1, g2, g3, g4 
build_graph(data=data, directed=True)