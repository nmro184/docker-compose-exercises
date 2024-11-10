from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

clock_app_url  = "http://clock_app:5001"

@app.route('/')
def button():
    return render_template("index.html")


@app.route('/subtract' , methods = ['POST' , 'GET'])
def subtract():
    response = requests.post(f'{clock_app_url}/decrement')
    if response.status_code == 200:
        return 'Time decremented successfully'
    else:
        return 'Failed to decrement time'

if __name__ == '__main__':
    app.run(debug=True , host = '0.0.0.0' , port =5002)
