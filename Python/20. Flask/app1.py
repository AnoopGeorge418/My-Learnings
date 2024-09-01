from flask import Flask

# wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
    return 'Welcome To Flask Learnings. This is awesome for Machine Learnings'

@app.route("/index")
def index():
    return 'Welcome To Index page'

# Entry point
if __name__ == "__main__":
    app.run(debug=True)