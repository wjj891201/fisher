from flask import jsonify, request, render_template, flash
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
            # result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            # result = BookViewModel.package_collection(result, q)
        # return jsonify(result)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)

    return render_template('search_result.html')


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    info = yushu_book.search_by_isbn(isbn)
    return render_template('book_detail.html', book=info[0], wishes=[], gifts=[])


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


@web.route('/test')
def test():
    r = {
        'name': 'wjp',
        'age': 18
    }
    flash('hello,qiyue')
    return render_template('test.html', data=r)
