CTakes(Clinical Text Analysis and Knowledge Extraction System)
cTAKES is an open-source natural language processing system for information extraction from electronic medical clinical free-text.cTAKES processes clinical notes, identifying entities from dictionaries(UMLS), and each entity has attributes, ontology mapping code, subject and context, partly relations.
The components of cTAKEs is specifically trained for clinical domain out of datasets, create rich linguistic and semantic antonations. In our project Real Time Drug Safety Monitoring in the Cloud, we use Twitter as a main source of public data sources to monitor and detect adverse drug effects, rather than a narrow set of applications on one or two ailments. ATAM(Aliment Topic Aspect Model) incorporating prior knowledge is the advanced model to create structured disease information from Tweets. 

Aliment Topic Aspect Model
In the graph shows above, tweets are identified by topic a, and topic a is a distribution over words f(a), the words are generated from different aspects，including general,symptom,treatment(y∈（0,1,2)),aspectes are being observed. ATAM includes another topic z distribution over words z, since these content are unrelated to sympton. Another switch table is needed here.
Switch Table 


cTakes is a specific application with the goal of learning new things form Twitter.







