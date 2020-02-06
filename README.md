# RecFIN-Data-Analysis-Project
This code takes data produced by RecFIN, does some statistical analysis on it in Python, and produces 
graphic representations of the data. I eventually want to find a way to integrate this data with QGIS 
in order to map it out.

To run this code, you must have SQLite installed and be able to use the sqlite3, csv, re, 
matplotlib.pyplot, collections and numpy python packages.



Explanations of files in repository:
  
  SEC Route List.txt
      
      List of sites with their site id numbers.
  
  80-16.csv
      
      CSV taken from RecFIN that contains all raw data. It is produced by going to the link at the bottom 
      of the RecFIN screen for 80-16.pdf and setting up the fields as shown in the pdf image. The data I'm
      using for this project is the data that has been collected from 1980 to 2016 for all shore fishing 
      modes at every site in the Channel Islands/Ventura/Santa Barbara district (District 2).
  
  sitedb.sqlite
      
      Database created running steps 1 and 2 above.  Cleaned up version of csv data.  Used by visualize.py
      and predict.py to perform analysis.
  
  createdb.py
      
      Creates clean sqlite database with tables Data and Sites from the 80-16.csv file by using the sqlite3,
      csv and re python packages. This database is used as the data source for all analysis.
      
  visualize.py

      Script collects data from a certain site and creates graphs of the total catch and Catch Per Unit 
      Effort (CPUE) across all months and years.  


  predict.py
      
      A script meant to make a prediction of the catch at a certain site for dates without data.  
  
  
