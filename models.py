import numpy as np
import pandas as pd
from fuzzywuzzy import process


data = pd.read_csv('static/sample.csv') 
df1 = pd.DataFrame(data=data)

# ------------------------- FUNCTIONS ------------------------- # 

def find_item(uinput, uquant):
    idx = process.extractOne(uinput, df1['product_name'])[2]

    item = df1['product_name'][idx]
    totalCarbs = (df1['carbohydrates_100g'][idx]/100.) * float(uquant)
    totalFat = (df1['fat_100g'][idx]/100.) * float(uquant)
    totalProtein = (df1['proteins_100g'][idx]/100.) * float(uquant)
    insulinReco = (df1['insulin_intake'][idx]/100.) * float(uquant)

    return item, round(totalCarbs,0), totalFat, totalProtein, insulinReco

# find_item('apple', 5)