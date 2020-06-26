import numpy as np
import pandas as pd
from fuzzywuzzy import process
import dataikuapi

# ------------------------- API ------------------------- # 
host = "https://wcsc1.dss-demo.dataiku.com/"
apiKey = "XCF82CIESH57BCLER0LG74YVIU8GLGSI"
client = dataikuapi.DSSClient(host, apiKey)

client.list_project_keys()

project = client.get_project("DATAFORCE")
dataset = project.get_dataset("python1_groomed") 

# ------------------------- API DATAFRAME ------------------------- # 
columns = [column['name'] for column in dataset.get_schema()['columns']]
row_count = 0
data = [ ]

for row in dataset.iter_rows():
    data.append(row)
    row_count = row_count + 1
    if row_count >= 10000:
        break

df1 = pd.DataFrame(data=data, columns=columns)

# ------------------------- CSV ------------------------- # 
# data = pd.read_csv('static/python1_groomed.csv') 
# df1 = pd.DataFrame(data=data)

# ------------------------- FUNCTIONS ------------------------- # 

def find_item(uinput, uquant):
    idx = process.extractOne(uinput, df1['product_name'])[2]

    item = df1['product_name'][idx]
    totalCarbs = (df1['carbohydrates_100g'][idx]/100.) * float(uquant)
    totalFat = (df1['fat_100g'][idx]/100.) * float(uquant)
    totalProtein = (df1['proteins_100g'][idx]/100.) * float(uquant)
    insulinReco = (df1['insulin_intake'][idx]/100.) * float(uquant)

    return item, int(totalCarbs), int(totalFat), int(totalProtein), int(insulinReco)

# find_item('apple', 5)