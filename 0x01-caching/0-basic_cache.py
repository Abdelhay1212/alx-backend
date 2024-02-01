#!/usr/bin/env python3
''' Basic dictionary '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' basic cache '''

    def put(self, key, item):
        ''' add item into the cache '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' get the value of a key from the cache'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
