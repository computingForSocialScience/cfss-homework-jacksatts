Instructions, Explanations

This project is definitely a doozy. 
Should everything had gone smoothly, the goal was to paint a picture of the situation of minorities and second language learners. The tables we drew data on were:

B01001. Sex by Age
B02001. Race
B16010. Educational Attainment and Employment Status by Language Spoken At Home for the Population 25 Years and Over 
B16009. Poverty Status in the Past 12 Months by Age by Language Spoken At Home for the Population 5+ Yrs 
B16008. Citizenship Status by Age by Language Spoken At Home for the Population 5+ Yrs 
B99163. Imputation of Ability to Speak English for the Population 5 Years and Over 


To "run" this project, first run the downloadscript.py 
This script is meant for data collection. There is code that should sift through the census data, and collect first the information from our targeted tables, and then the data housed in each of these tables (for all of the states for which we were provided FIPS Codes).

Ultimately, this script was met with many issues in collecting public data. Unfortuately, the error occured while trying to create a list that will be used to import into a local MySQL table. I could only populate my "Table Information" table, and not the a table for the actual data.
Now, in the attempts of fixing in initial append issue (the lists were being expanded laterally instead of very long list of 6-tuples), the code takes so long to scrape all the data that the connection is aborted before completion. This could possibly be due to attempting to collect data from all the states instead of choosing a select few. That is a large request to make at one time.

Without concrete data, it has been difficult to continue. 
The next step in the execution of this project would be to run applicaiton.py
This code is the bare bones of making a working application. It is hard to determine which variable plugs in to the code that creates the comparison scatterplot and table for analysis, when there is no way to check how our data was imported. For that reason, there are many gaps and placeholder variables in this code. For example, the analysis of the data cannot be done first because I was unable to merge the two tables of information into a third table of all of my data. Additionally, it is difficult to predetermine what these variables would be called/how they would be manipulated into dataframes to be analysed using pandas, finding means, or using bokeh. The two html codes im my templates folder reflect this as well.

I have been trouble shooting both on my own and at TA sessions, but this is where my progress leaves me. Thank you for your help. I wish I had more to show for it.