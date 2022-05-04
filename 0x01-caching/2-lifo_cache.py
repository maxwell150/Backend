#!/usr/bin/python3
"""LIFOCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                keys = list(self.cache_data.keys())
                print("DISCARD: {}".format(keys[-1]))
                del self.cache_data[keys[-1]]
                self.cache_data[key] = item

    def get(self, key):
        """get
        """
        if key:
            return self.cache_data.get(key)
        return None
