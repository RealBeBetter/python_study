# encoding: utf-8
import re

from basic_syntax.oriented_object.search_engine.SearchEngineBase import SearchEngineBase, main


class BowEngine(SearchEngineBase):
    def __init__(self):
        super(BowEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, text_id, text):
        self.__id_to_words[text_id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for text_id, words in self.__id_to_words.items():
            if query_words.issubset(words):
                results.append(text_id)
        return results

    @staticmethod
    def parse_text_to_words(text) -> set:
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)


search_engine = BowEngine()
main(search_engine)
