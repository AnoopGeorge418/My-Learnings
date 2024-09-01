# Building own dynamic url
# Variable rule
# Jinja 2 Template Engine:
'''
    {{ }} - expression to print output in html
    {% %} - conditions, loops
    {# #} - comments
'''

from flask import Flask, render_template, request

# wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
    return '<html><h1>Welcome To Flask Learnings. This is awesome for Machine Learnings</h1></html>'

@app.route("/index", methods  = ['GET'])
def index():
    return render_template('index.html')

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'
        
    return render_template('results.html', results = res)

@app.route('/success_results/<int:score>')
def success_results(score):
    res = ''
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'
        
    exp = {'Score': score, 'Result': res}
        
    return render_template('results1.html', results = exp)

# Entry point
if __name__ == "__main__":
    app.run(debug=True)