#!/usr/bin/env python3
"""first tutoiral of retierve chace from dict"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """inherit from the parent class BaseCaching"""
    def __init__(self):
        self.cache_data = OrderedDict()
        super().__init__()

    def put(self, key, item):
        """Put in the dict"""
        if key is not None and item is not None:
            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(key, "default value")
                print(f"DISCARD: {key}")
            self.cache_data[key] = item

    def get(self, key):
        """Get from the dict"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
