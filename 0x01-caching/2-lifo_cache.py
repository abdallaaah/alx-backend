#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """class inherit from the parent"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """the put in the dictt function"""
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discard[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """the get function from chache dict"""

        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
