#!/usr/bin/env python3
''' MRU Caching '''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' MRU cache '''

    def __init__(self):
        self.mru = []
        super().__init__()

    def put(self, key, item):
        ''' add item into the cache '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.mru.remove(key)
                self.mru.insert(0, key)
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_recently_used = self.mru.pop(0)
                    del self.cache_data[least_recently_used]
                    print('DISCARD: {}'.format(least_recently_used))
                self.mru.insert(0, key)
                self.cache_data[key] = item

    def get(self, key):
        ''' get the value of a key from the cache'''
        if key is not None and key in self.cache_data:
            self.mru.remove(key)
            self.mru.insert(0, key)
            return self.cache_data[key]
        return None
