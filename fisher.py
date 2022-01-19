from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


# @app.route('/hello')
# def hello():
#     headers = {
#         'content-type': 'application/json',
#         'location': 'http://www.baidu.com'
#     }
#     # response = make_response('<html></html>', 301)
#     # response.headers = headers
#     # return '<html></html>', 301, headers
#     return 'Hello, QiYue3'


# app.add_url_rule('/hello', view_func=hello)

@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    pass


if __name__ == '__main__':
    # 生产环境 nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=2000)
