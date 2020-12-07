# 2019-Weather-Data-Wrangling

After completing a data scientist professional certificate with IBM and Coursera I wanted to work on a real project and chose to volunteer to work as a part-time data analyst for an environmental consultancy.

This notebook is about combining a number of data from the Australian Bureau of Meteorology(BoM) in order to present an hourly average, min, max temperatures and precipitations for a given weather station in Australia. The output is a csv file containing all these information.

It seemed important to clean and organize these data as the original format did not allow any analysis. Indeed, the raw data are a combination of 730 csv files (one for each day from 20160501 to 20180430), each containing approximately 48,000 rows. So it is about 34,000,000 rows to aggregate, clean and reorganize in a format that can be used for local weather analysis. End goal being to run some energy savings scenarii.

I attach a sample of input and output of data.

Please do not hesitate to suggest any way to improve the code!
