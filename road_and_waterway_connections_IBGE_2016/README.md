# Brazil road and waterway connections IBGE 2016

Data on road and waterway connections are available at [this link](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/redes-e-fluxos-geograficos/15794-rodoviarias-e-hidroviarias?=&t=downloads). Containing municipalities not subject to
search: contains a list of municipalities whose links were not raised due to that there is no public transport or that the agents responsible for transport do not correspond to the requirements of regularity necessary for the collection. Also contains a brief description of how transportation is carried out in the municipalities - centrality indexes: contains two tables. The first presents indexes of proximity, intermediation and degree, for the set of municipalities surveyed (5,386), calculated from network analysis using graph theory. The second presents the centrality index and the average cost by time for 244 higher ranking urban centers (from sub-regional centers above), from REGIC 2007. - Database - road and waterway connections 2016: It constitutes the core of the research, containing the pairs of links aggregated between municipalities. Frequencies were aggregated, round trip, as well as redundant sections, for each pair of municipalities connected by transport lines. Considering the costs and minimum travel time.

We provide the networks built from these files in GraphML format, including geographic coordinates and scripts to plot them according to the networks generated in GraphML.
 
### Data organization: 
- input data: In this folder you will find folders called networks, raw data and also a python file which is the code to generate the network in GraphML. In the raw data folder are the data that will be processed to generate the respective network and the data after processing will also be saved and the networks generated in GraphML will be saved in the network folder.

- results: In this folder you will find a folder called metrics. In the metrics folder there will be folders for each network that will be generated: complete graph, hydro weight graph, squeegee weight graph, summed weight graph and each folder will have the appropriate specifications for each type of trip cost, in, out, time. They will have their plots saved in png and xlsx with the travel locations.

- scr: In this folder you will find three python files which are the codes to plot the networks.

### Source code:
