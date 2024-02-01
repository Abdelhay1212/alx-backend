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
            if key in self.cache_data:
                self.lru.remove(key)
                self.lru.append(key)
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_recently_used = self.lru.pop(0)
                    del self.cache_data[least_recently_used]
                    print('DISCARD: {}'.format(least_recently_used))
                self.lru.append(key)
                self.cache_data[key] = item

    def get(self, key):
        ''' get the value of a key from the cache'''
        if key is not None and key in self.cache_data:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache_data[key]
        return None
