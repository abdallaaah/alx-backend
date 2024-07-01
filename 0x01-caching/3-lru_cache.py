#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """inherit from the parent basechae"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """the put in the dict function"""
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discard[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """the get function from chache dict"""

        if key is None or key not in self.cache_data.keys():
            return None
        x = self.cache_data[key]
        self.cache_data.move_to_end(key, last=True)
        return x
