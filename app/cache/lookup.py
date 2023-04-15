from .lru import LRUCache

import json
from ..config import settings


class Lookup:
    def __init__(self, size, ttl):
        self.lru = LRUCache(size, ttl)

    def __getLRU(self, key):
        return self.lru.get(key)

    def __setLRU(self, key, value):
        self.lru.put(key, value)

    def set(self, key, value):
        self.__setLRU(key, value)
        return self.get(key)

    def get(self, key):
        result = self.__getLRU(key)
        if result:
            return result
        return None


lookup = Lookup(settings.lru_size, settings.ttl)
