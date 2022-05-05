#!/usr/bin/env python3
""" LFUCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.map = {}

    def put(self, key, item):
        """put
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                keys = self.cache_data.keys()
                count = self.map.keys()
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.map[key] += 1
                else:
                    self.cache_data[key] = item
                    self.map[key] = 1
                t_keys = [(key, self.cache_data[key]) for key in keys]
                self.cache_data = OrderedDict(t_keys)
                t_count = [(key, self.map[key]) for key in count]
                self.map = OrderedDict(t_count)

            else:
                if key not in self.cache_data:
                    minkey = min(self.map, key=self.map.get)
                    del self.cache_data[minkey]
                    print("DISCARD: {}".format(minkey))
                    del self.map[minkey]
                    self.cache_data[key] = item
                    self.map[key] = 1
                else:
                    self.cache_data[key] = item
                    self.map[key] += 1

    def get(self, key):
        """get
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=True)
        self.map[key] += 1
        self.cache_data.move_to_end(key, last=True)
        return self.cache_data[key]
