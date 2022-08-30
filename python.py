### import packages
import pandas as pd
import xlrd
import json
import requests
from google.cloud import bigquery 

### section 1
## bring in excel file
df = pd.read_excel('/Users/sairakhwaja/Documents/python/hha507_fake_data.xlsx')
## define tab1 and tab2 as sheet1 and sheet2
tab1 = pd.read_excel('/Users/sairakhwaja/Documents/python/hha507_fake_data.xlsx', sheet_name='Sheet1')
tab2 = pd.read_excel('/Users/sairakhwaja/Documents/python/hha507_fake_data.xlsx', sheet_name='Sheet2')


### section 2
## bring in open source JSON API via CMS using REQUESTS function
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/8c7fac95-aaec-4233-bad5-ac51d0f2dfc9/data')
## define apiDataset as JSON file
apiDataset = apiDataset.json()


### section 3
gcp_project = 'hha-507-data-ingestion'
## connect to gcp
client = bigquery.Client.from_service_account_json('/Users/sairakhwaja/Downloads/hha-507-data-ingestion-ad35f0013862.json')
## define query_job variable to access pub. db. & limit to first 100 rows
query_job = client.query("SELECT * FROM `bigquery-public-data.austin_311.311_service_requests` LIMIT 100")
results = query_job.result()
## define bigquery1 and convert results to df
bigquery1 = pd.DataFrame(results.to_dataframe())
## repeat 3 prev lines for dataset2
query_job2 = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")
results2 = query_job2.result()
bigquery2 = pd.DataFrame(results2.to_dataframe())