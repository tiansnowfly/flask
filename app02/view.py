from app02 import app
from flask import render_template,url_for,redirect,flash

@app.route('/')
def hello_world():
    user = {'username': 'snow fly'}
    posts = [{
        'author': {'username': 'snow'},
        'body': 'Beautiful day in Portland!'
    },
        {
            'author': {'username': 'fly'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8001)