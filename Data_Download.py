# Download the file from `url` and save it locally under `file_name`
# Tacoma Permits from CivicData (json)
# Don't download any records without a lat/long.
# Updated: 2019-9-4
# Author: mmurnane

#import urllib
import urllib.request
import logging
import os

#permitsResourceId = "b40a095a-e03a-4b1c-a2cb-f999b3838e0b" #Changed 2019-9-4
permitsResourceId = "9474d5f7-fac8-451a-8e48-93a9ae6d6077" #Changed 1/7/2020 - http://www.civicdata.com/dataset/mapdata_v3_17678/resource/9474d5f7-fac8-451a-8e48-93a9ae6d6077

theFields = "%22Permit_Number%22,%22Applied_Date%22,%22Latitude%22,%22Longitude%22,%22Address_Line_1%22,%22Permit_Type_Description%22,%22Current_Status%22,%22Issued_Date%22,%22Fees_Paid%22,%22Valuation%22,%22Description%22,%22Link%22"

#ALL PERMITS - 9.5 seconds browser load time
url = 'http://www.civicdata.com/api/3/action/datastore_search_sql?sql=SELECT%20' + theFields + '%20FROM%20%22' + permitsResourceId + '%22%20where%20%22Latitude%22%20%3C%3E%27%27%20and%20%22Longitude%22%20%3C%3E%20%27%27'

#Last 30 days - 7.5 seconds
#url = 'http://www.civicdata.com/api/3/action/datastore_search_sql?sql=SELECT%20' + theFields + '%20FROM%20%22' + permitsResourceId + '%22%20where%20%22Latitude%22%20%3C%3E%27%27%20and%20%22Longitude%22%20%3C%3E%20%27%27and%20%22Applied_Date%22%20%3E%20%272019-01-29%27'

#file_name = "\\\\wsitd01dev\\c$\\GADS\\website\\PDS\\Permits\\data\\Permits.json"  #DEV machine
file_name = "\\\\wsitd01\\c$\\GADS\\website\\PDS\\Permits\\data\\Permits.json"  #Production machine

try:
  # Download file 
  #urllib.urlretrieve (url, file_name)
  print("Downloading Permit json data ...")
  urllib.request.urlretrieve(url, file_name) # Download the file from `url` and save it locally under `file_name`
except:
  logging.exception('\n Unexpected error with website, could not download file successfully: \n')
else:
  if os.path.getsize(file_name)> 10000000:
    print("File download successful!")
  else:
    print("CHECK JSON FILE FOR ERROR MESSAGE! File download successful, but file size appears too small!")
