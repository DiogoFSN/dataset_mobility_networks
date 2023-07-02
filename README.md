# dataset_mobility_networks
 
# Sao Paulo metro 2017

The Sao Paulo metro 2017 data is available at [this link](https://www.metro.sp.gov.br/pesquisa-od/). It contains the numbers of trips from traffic zones in the metropolitan area of Sao Paulo, Brazil, distinguishing different transport modes, namely on foot, by car, by bicycle, using collective transport, individual and non-motorized transport. For each transport mode, there is a weighted adjacency matrix in a xlsx file. 

We provide the networks built from this file in GraphML format, including geographical coordinates and scripts to plot them according to the networks generated in GraphML.

# Brazil road and waterway connections IBGE 2016

Data on road and waterway connections are available at [this link](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/redes-e-fluxos-geograficos/15794-rodoviarias-e-hidroviarias?=&t=downloads). Containing municipalities not subject to
search: contains a list of municipalities whose links were not raised due to that there is no public transport or that the agents responsible for transport do not correspond to the requirements of regularity necessary for the collection. Also contains a brief description of how transportation is carried out in the municipalities - centrality indexes: contains two tables. The first presents indexes of proximity, intermediation and degree, for the set of municipalities surveyed (5,386), calculated from network analysis using graph theory. The second presents the centrality index and the average cost by time for 244 higher ranking urban centers (from sub-regional centers above), from REGIC 2007. - Database - road and waterway connections 2016: It constitutes the core of the research, containing the pairs of links aggregated between municipalities. Frequencies were aggregated, round trip, as well as redundant sections, for each pair of municipalities connected by transport lines. Considering the costs and minimum travel time.

We provide the networks built from these files in GraphML format, including geographic coordinates and scripts to plot them according to the networks generated in GraphML.

# Intermunicipal travel networks of Mexico during the COVID-19 pandemic

Data on intermunicipal travel networks of Mexico during the COVID-19 pandemic are available at [this link](https://www.nature.com/articles/s41598-023-35542-5). Containing a more complete explanation about all the research carried out, where a public dataset of 731 intercity networks of origin-destination in Mexico were used, each network is represented for each day during the period 2020-2021, describing the patterns of trips made between municipalities in Mexico in the period 2020-2021, using anonymized mobile location data. In which characteristic changes associated with factors such as COVID-19 restrictions and population size were observed. The nodes represent municipalities (third-level administrative division) or official metropolitan areas. These are weighted and directed networks, where the weight of the edge ( i , j ) is equal to the total number of observed trips from node i to node j normalized by the different number of mobile devices we registered that day. The dataset with these 731 networks is freely available in an OSF repository [this link](http://dx.doi.org/10.17605/OSF.IO/42XQZ).

Finally, nine plotted dates were made available to represent different important events during the evolution of the pandemic in Mexico, as well as explanations of the necessary changes for each plot.

# Research Origin and Household Destination of the Metropolitan Region of Salvador (RMS) 2012

Data on the Survey Origin and Household Destination of the Metropolitan Region of Salvador (RMS) 2012 are available at [this link](http://www.infraestrutura.ba.gov.br/modules/conteudo/conteudo.php?conteudo=16). Containing a more complete explanation of all the research carried out, where this research aimed to collect updated information about the displacements made by the population on a typical working day. The Metropolitan Region of Salvador concentrates around 3.88 million people, spread over an area of approximately 4,385 km².
An important characteristic of the Origin and Destination Survey is that it allows the spatial location of the population, jobs, school enrollments and the origins and destinations of trips made by the RMS population in their daily activities. The Metropolitan Region of Salvador, made up of 13 municipalities, was divided into 232 research zones. The municipality of Salvador alone was divided into 152 research zones. The main criteria for defining the 2012 zoning were the following:
- Compatibility with municipal boundaries
- Consideration of IBGE 2010 census tract limits
- The transport system, urban equipment, physical barriers and empty areas were also considered in the zoning.

Finally, in this research, no graph of the trips made was generated, but in the research results several metrics used in the research can be found that can be used in the future to generate the graph.
