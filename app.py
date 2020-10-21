from flask import Flask, render_template, send_from_directory
from extract import jokes
from image import *
import os

app = Flask(__name__)

@app.route('/')

def main():
	textimg()
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)