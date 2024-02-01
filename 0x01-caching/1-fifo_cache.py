#!/usr/bin/env python3
''' FIFO caching '''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFO cache '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' add item into the cache '''
        if key is not None and item is not None:
            if key not in self.cache_data and\
                    len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print('DISCARD: {}'.format(first_key))
                del self.cache_data[first_key]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        ''' get the value of a key from the cache'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
