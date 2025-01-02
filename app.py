import os
import redis
from flask import Flask

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'redis')  # Default to 'redis' if not set in env
redis_port = int(os.getenv('REDIS_PORT', 6379))  # Default to 6379
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True)

@app.route('/')
def visit_count():
    # Increment visit count in Redis
    count = redis_client.incr('visit_count')
    return f"Hello! You've visited this page {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)