from flask import Flask, render_template, request, jsonify
import requests
import os 

app = Flask(__name__)

clock_app_url = os.getenv("CLOCK_APP_URL","http://clock_app") # Update with the actual URL of the clock app

@app.route('/')
def index():
    return render_template('button_index.html')

@app.route('/decrement_time', methods=['POST'])
def decrement_time():
    minutes_to_subtract = int(request.form['minutes'])
    
    # Make API call to clock app to decrement the time
    response = requests.post(f'{clock_app_url}/update_time', data={'minutes': minutes_to_subtract})
    
    if response.status_code == 200:
        return 'Time decremented successfully'
    else:
        return 'Failed to decrement time'

if __name__ == '__main__':
    app.run(debug=True, port=80,host="0.0.0.0")