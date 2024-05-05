# encoding: utf-8

from basic_syntax.oriented_object.search_engine.SearchEngineBase import SearchEngineBase, main


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, text_id, text):
        self.__id_to_texts[text_id] = text

    def search(self, query):
        results = []
        for text_id, text in self.__id_to_texts.items():
            if query in text:
                results.append(text_id)
        return results


search_engine = SimpleEngine()
main(search_engine)
