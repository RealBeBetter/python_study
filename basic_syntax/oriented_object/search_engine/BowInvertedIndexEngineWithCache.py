# encoding: utf-8

import pylru

from basic_syntax.oriented_object.search_engine.BowInvertedIndexEngine import BowInvertedIndexEngine
from basic_syntax.oriented_object.search_engine.SearchEngineBase import main


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value


class BowInvertedIndexEngineWithCache(BowInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BowInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)

        result = super(BowInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)

        return result


search_engine = BowInvertedIndexEngineWithCache()
main(search_engine)
