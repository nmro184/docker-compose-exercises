from flask import Flask, render_template
import redis

app = Flask(__name__)

# Connect to the Redis server
redis_host = 'redis-server'  # replace with your Redis server's host
redis_port = 6379  # replace with your Redis server's port

# Create a Redis connection
redis_conn = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

# Define the key for the page counter in Redis
page_counter_key = 'page_counter'

@app.route('/')
def index():
    # Increment the page counter in Redis
    page_count = redis_conn.incr(page_counter_key)

    return render_template('index.html', page_count=page_count)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
