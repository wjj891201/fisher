from flask import jsonify, request
from app.forms.book import SearchForm

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    # q = request.args['q']
    # page = request.args['page']

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)

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
