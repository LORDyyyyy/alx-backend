#!/usr/bin/env python3
""" LIFO cache dictionary """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        A LIFO caching system.
    """

    def __init__(self):
        """ init function """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            del self.cache_data[key]
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > super().MAX_ITEMS:
            removed_key = list(self.cache_data.keys())[-2]
            print(f'DISCARD: {removed_key}')
            del self.cache_data[removed_key]

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """

        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
