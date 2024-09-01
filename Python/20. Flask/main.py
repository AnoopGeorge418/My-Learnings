from flask import Flask, render_template

# wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
    return '<html><h1>Welcome To Flask Learnings. This is awesome for Machine Learnings</h1></html>'

@app.route("/index")
def index():
    return render_template('index.html')

# Entry point
if __name__ == "__main__":
    app.run(debug=True)