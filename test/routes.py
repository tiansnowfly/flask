from flask import render_template, flash, redirect, url_for, request, jsonify
from werkzeug.utils import secure_filename
import json
from test import app
import os
import pandas as pd

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request_data', methods=['POST'], strict_slashes=False)
def api_upload():
    basedir=os.path.dirname(__file__)
    file_dir = os.path.join(basedir, 'static','json')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    elif os.path.exists(file_dir):
        file_name=os.path.join(file_dir,'test.json')
        jsonTest=pd.read_json(file_name)
        print(url_for('api_upload'))
        with open(file_name,'r') as f:
            content=f.readlines()
            content=json.loads(content[0])
            f.close()
        # 返回请求的类型返回的类型还不能是numpy.int32
        return jsonify(content)
    else:
        return jsonify({"error": 'error', "msg": "请求失败"})

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=7997)