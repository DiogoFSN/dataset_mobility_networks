# dataset_mobility_networks
 
# Sao Paulo metro 2017

The Sao Paulo metro 2017 data is available at [this link](https://www.metro.sp.gov.br/pesquisa-od/). It contains the numbers of trips from traffic zones in the metropolitan area of Sao Paulo, Brazil, distinguishing different transport modes, namely on foot, by car, by bicycle, using collective transport, individual and non-motorized transport. For each transport mode, there is a weighted adjacency matrix in a xlsx file. 

We provide the networks built from this file in GraphML format, including geographical coordinates and scripts to plot them according to the networks generated in GraphML.

# Brazil road and waterway connections IBGE 2016

Data on road and waterway connections are available at [this link](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/redes-e-fluxos-geograficos/15794-rodoviarias-e-hidroviarias .html?=&t=what-is). Containing municipalities not subject to
search: contains a list of municipalities whose links were not raised due to that there is no public transport or that the agents responsible for transport do not correspond to the requirements of regularity necessary for the collection. Also contains a brief description of how transportation is carried out in the municipalities - centrality indexes: contains two tables. The first presents indexes of proximity, intermediation and degree, for the set of municipalities surveyed (5,386), calculated from network analysis using graph theory. The second presents the centrality index and the average cost by time for 244 higher ranking urban centers (from sub-regional centers above), from REGIC 2007. - Database - road and waterway connections 2016: It constitutes the core of the research, containing the pairs of links aggregated between municipalities. Frequencies were aggregated, round trip, as well as redundant sections, for each pair of municipalities connected by transport lines. Considering the costs and minimum travel time.

We provide the networks built from these files in GraphML format, including geographic coordinates and scripts to plot them according to the networks generated in GraphML.
