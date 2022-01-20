class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        pass

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'author': '、'.join(data['author']),
            'binding': data['binding'],
            'publisher': data['publisher'],
            'image': data.image,
            'price': data['price'],
            'isbn': data.isbn,
            'pubdate': data['pubdate'],
            'summary': data['summary'],
            'pages': data['pages']
        }
        return book
