#!/usr/bin/env python3
"""a class BasicCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_cache').BaseCaching

class BasicCache(BaseCaching):
    """basic cache
    """
    def __init__(self):
        """initialize
        """
        super().__init__()

    def put(self, key, item):
        """put
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get
        """
        if key:
            return self.cache_data.get(key)
        return None


