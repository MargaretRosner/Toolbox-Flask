"""
Simple "Hello, World" application using Flask
"""


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()




if __name__ == '__main__':
    app.run()
