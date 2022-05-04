#!/usr/bin/python3
""" LRUCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache
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
                if key not in self.cache_data:
                    keys = list(self.cache_data.keys())
                    print("DISCARD: {}".format(keys[0]))
                    del self.cache_data[keys[0]]
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)

    def get(self, key):
        """get
        """
        if key and self.cache_data.get(key):
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
