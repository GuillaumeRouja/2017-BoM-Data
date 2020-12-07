# 2019-Weather-Data-Wrangling

After completing a data scientist professional certificate with IBM and Coursera I wanted to work on a real project and chose to volunteer to work as a part-time data analyst for an environmental consultancy.

This notebook is about combining a number of data from the Australian Bureau of Meteorology(BoM) in order to present an hourly average, min, max temperatures and precipitations for a given weather station in Australia. The output is a csv file containing the cleaned data for a particular area.

It seemed important to clean and organize these data as the original format mixed various data, many of which were not relevant for the study. 
The raw input data are a combination of 730 csv files (one for each day from 20160501 to 20180430), each containing approximately 48,000 rows. So it is about 34,000,000 rows that i needed to aggregate, clean and reorganize in a format that could be used for local weather analysis. End goal being to run some energy savings predictions.

I attach an input sample (one of the 730 csv files) and the output csv file for the station of Canberra.

Please do not hesitate to suggest any way to improve the code!
