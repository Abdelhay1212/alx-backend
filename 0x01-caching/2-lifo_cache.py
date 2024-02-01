#!/usr/bin/env python3
'''  LIFO Caching '''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFO cache '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' add item into the cache '''
        if key is not None and item is not None:
            if key not in self.cache_data and\
                    len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                print('DISCARD: {}'.format(last_key))
                del self.cache_data[last_key]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        ''' get the value of a key from the cache'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
