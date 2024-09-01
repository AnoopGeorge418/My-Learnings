from flask import Flask, render_template, request

# wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
    return '<html><h1>Welcome To Flask Learnings. This is awesome for Machine Learnings</h1></html>'

@app.route("/index", methods  = ['GET'])
def index():
    return render_template('index.html')

@app.route("/form", methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Entry point
if __name__ == "__main__":
    app.run(debug=True)