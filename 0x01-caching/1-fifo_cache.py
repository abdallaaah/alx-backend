#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """the put in the dict function"""
        if key is None or item is None:
            pass
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            discard = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discard[0]}")
        self.cache_data[key] = item
        # print(f"{key} addedd")

    def get(self, key):
        """the get function from chache dict"""

        if key is not None or key not in self.cache_data.keys():
            return self.cache_data[key]
