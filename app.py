import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, json, Response, send_file
from models import find_item
from fuzzywuzzy import process

app = Flask(__name__)


data = pd.read_csv('static/python1_groomed.csv') 
df1 = pd.DataFrame(data=data)

# ['product_name', 'fat_100g', 'carbohydrates_100g', 'proteins_100g', 'carb_classifier', 'insulin_intake']

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