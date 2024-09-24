from flask import Flask
import os
import time 
import redis 

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            #cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as excp:
            if retries == 0:
                raise excp
            retries -= 1
            time.sleep(0.5)

@app.route('/', methods = ['GET'])
def home():
    count = get_hit_count()
    return f'Hello Anoop George! I have been seen {count} times.'

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port = 5000)