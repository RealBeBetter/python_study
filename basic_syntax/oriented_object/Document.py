# encoding: utf-8

class Document(object):
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context  # __ 开头的属性是私有属性

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]


harry_potter_book = Document('Harry Potter', 'J. K. Rowling',
                             '... Forever Do not believe any thing is capable of thinking independently ...')

print(harry_potter_book.title)  # Harry Potter
print(harry_potter_book.author)  # J. K. Rowling
print(harry_potter_book.get_context_length())  # 77

harry_potter_book.intercept_context(10)  # 截取前 10 个

print(harry_potter_book.get_context_length())  # 10
print(harry_potter_book.__context)
# Traceback (most recent call last):
#   File "C:\Users\Xxx\Document.py", line 28, in <module>
#     print(harry_potter_book.__context)
# AttributeError: 'Document' object has no attribute '__context'
