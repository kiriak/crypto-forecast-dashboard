from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    images = [img for img in os.listdir('.') if img.endswith('_forecast.png')]
    return render_template('index.html', images=images)


