#!/usr/bin/env python3
""" LRU cache dictionary """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
        A LRU caching system.
    """

    def __init__(self):
        """ init function """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            del self.cache_data[key]
        elif len(self.cache_data.keys()) >= super().MAX_ITEMS:
            removed_key = self.cache_data.popitem(last=False)
            print(f'DISCARD: {removed_key[0]}')
        self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """

        if key is None or key not in self.cache_data.keys():
            return None
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = val
        return self.cache_data.get(key)
