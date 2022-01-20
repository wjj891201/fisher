from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    isbn_url = 'http://localhost:3000/fisher?isbn={}'
    keyword_url = 'http://localhost:3000/fisher?q={}&_limit={}&_start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
