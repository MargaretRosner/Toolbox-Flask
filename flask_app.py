"""
Put your Flask app code here.
"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['firstname'] and request.form['age'] and request.form['faveninja']:
            error = None
            return render_template('login.html', firstname=request.form['firstname'], age=request.form['age'])
        else:
            error = 'Invalid username/password'
            render_template('index.html')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
if __name__ == '__main__':
    app.run()
