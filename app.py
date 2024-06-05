from flask import Flask, render_template, redirect, url_for, jsonify
import subprocess
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['twitter_trends_scrapping']
collection = db['top_trends']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    subprocess.run(["python", "scraper.py"])
    return redirect(url_for('show_results'))

@app.route('/show_results')
def show_results():
    latest_record = collection.find().sort('_id', -1).limit(1)[0]
    return render_template('results.html', data=latest_record)
