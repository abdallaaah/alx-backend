#!/usr/bin/env python3
"""first tutoiral of retierve chace from dict"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """inherit from the parent class BaseCaching"""
    def __init__(self):

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put in the dict"""
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discard}")
            self.cache_data[key] = item
        else:
            return

    def get(self, key):
        """Get from the dict"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
