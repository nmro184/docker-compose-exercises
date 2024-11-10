from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

time = datetime.now()

@app.route('/decrement' , methods = ['POST'])
def decrement():
    global time  
    time = time - timedelta(minutes=1)
    return f"Time decremented by 1 minute: {time}"

@app.route('/')
def clock():
    return render_template('index.html', time=time)

if __name__ == '__main__':
    app.run(debug=True , host = '0.0.0.0' , port =5001)
