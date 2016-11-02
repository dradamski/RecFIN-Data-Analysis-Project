# RecFIN-Data-Analysis-Project
This code takes data produced by RecFIN, does some statistical analysis on it, and produces graphic representations of the data.

The 80-16.csv file is produced by going to the link at the bottom of the RecFIN screen for 80-16.pdf and setting up the fields as shown in the pdf image. The data I'm using for this project is the data that has been collected from 1980 to 2016 for all shore fishing modes at every site in the Channel Islands/Ventura/Santa Barbara district (District 2).

The order this code should be run in as of right now to produce the proper results:
  1. data2db.py (pulls data from 80-16.csv)
  2. site2db.py (pulls data from SEC Route List.txt)
  3. add_site_id_to_data_db.py
  4.
  5.
 
Explanations of code not run above:
  predict.py is a script meant to make a prediction of the catch at a certain site for dates without data.  
   It needs a lot of work because my statistics skills are a little rusty.  However, I hope to figure out 
   whether this is done correctly, 
