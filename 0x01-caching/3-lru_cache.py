#!/usr/bin/env python3
''' LRU Caching '''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRU cache '''

    def __init__(self):
        self.lru = []
        super().__init__()

    def put(self, key, item):
        ''' add item into the cache '''
        if key is not None and item is not None:
            if key not in self.cache_data and\
                    len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                self.lru.append(key)
                least_key_used = self.lru.pop(0)
                print('DISCARD: {}'.format(least_key_used))
                del self.cache_data[least_key_used]
                self.cache_data[key] = item
            elif key in self.cache_data:
                for i, k in enumerate(self.lru):
                    if k == key:
                        del self.lru[i]
                self.lru.append(key)
            else:
                self.lru.append(key)
                self.cache_data[key] = item

    def get(self, key):
        ''' get the value of a key from the cache'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
