import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, json, Response, send_file
from models import find_item
from fuzzywuzzy import process
import dataikuapi


app = Flask(__name__)

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


# ------------------------- ROUTES ------------------------- # 
@app.route('/')
def main():
    return render_template("InsulnX.html")

@app.route('/get_id', methods=['POST'])
def finder():
    
    # User_pick
    user_item = request.form['meal']
    user_portion = request.form['sizeofportion']
    
    food = find_item(user_item, user_portion)
    
    return render_template("index.html", food=food)


if __name__ == "__main__":
    # For local development, set to True
    app.run(debug=True)