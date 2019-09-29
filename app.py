"""
@author:yeliulee | 夜琉璃
@LICENSE:@2019 yeliulee
@contact:yeliulee@qq.com | QQ2813361953
@software:Pycharm
@time:2019-09-29 04:37:24
"""

import os
import json
import random
from flask import Flask, render_template, request, abort

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_data')
def get_data():
    # 判断请求来路域名，防止采集和盗链
    if '127.0.0.1' not in str(request.referrer):
        abort(403)
    else:
        data_file_path = os.path.join(APP_ROOT, 'static/data/data.json')
        with open(data_file_path, 'r', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            temp_data_list = random.sample(data, 1)
            temp_data = temp_data_list[0]
            return str(temp_data)


# 防止直接获取到数据文件
@app.route('/static/data/data.json')
def not_allowed():
    abort(403)


if __name__ == '__main__':
    app.run()
