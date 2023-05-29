Open data from the São Paulo state metro mobility network collected in 2017 was utilized, along with a file provided by Professor Vander Luis containing the centroids of each neighborhood in the city of São Paulo. These centroids represent the number of trips between neighborhoods using various modes of transportation, along with the coordinates of each neighborhood.

To work with this data, files in xlsx and csv formats were used, and data cleaning was performed to exclude rows and columns that were not relevant for constructing the graph. Columns that encompassed other cities in the state of São Paulo were removed.

Furthermore, the attribute file provided by the professor only contained the coordinates of the city's neighborhoods. The libraries pandas, numpy, igraph, and os were employed for analysis. 

Consequently, a single-layer directed graph without weights was obtained.
