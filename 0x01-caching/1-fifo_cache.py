#!/usr/bin/env python3
""" class FIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache
    """
    def __init__(self):
        """intializer
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assugn the cache
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
                keys = list(self.cache_data.keys())
                print("DISCARD: {}".format(keys[0]))
                del self.cache_data[keys[0]]

    def get(self, key):
        """return val in self.cache_data linked to key
        """
        if key:
            return self.cache_data.get(key)
        return None


