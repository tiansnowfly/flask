from app01 import app # 从app01包中导入实例化的app应用程序对象
from flask import render_template,url_for,flash,redirect
from app01.form import LoginForm

@app.route('/')
def index():
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
    return render_template("index.html",title='Home',user=user,posts=posts)

@app.route('/form',methods=['GET','POST'])
def formPage():
    print('hello')
    # form=LoginForm()
    # # 表单被提交的时候进行调用
    # if form.validate_on_submit():
    #     # 将消息刷新到下一个请求
    #     flash('Login requested for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     return redirect(url_for('index'))
    # return render_template('form.html',title='sign in',form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=7999)
