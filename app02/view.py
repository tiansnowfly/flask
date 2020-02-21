from app02 import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8001)