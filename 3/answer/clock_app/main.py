from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

current_time = datetime.now()

@app.route('/')
def index():
    return render_template('clock_index.html', current_time=current_time)

@app.route('/update_time', methods=['POST'])
def update_time():
    global current_time
    minutes_to_subtract = int(request.form['minutes'])
    current_time -= timedelta(minutes=minutes_to_subtract)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=80,host="0.0.0.0")
