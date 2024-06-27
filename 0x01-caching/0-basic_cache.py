#!/usr/bin/env python3
from base_caching import BaseCaching
"""first tutoiral of retierve chace from dict"""


class BasicCache(BaseCaching):
    """inherit from the parent class BaseCaching"""
    def put(self, key, item):
        """Put in the dict"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get from the dict"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
