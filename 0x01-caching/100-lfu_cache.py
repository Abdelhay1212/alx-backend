#!/usr/bin/env python3
''' LFU Caching '''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' LFU Caching '''

    def __init__(self):
        self.luf = {}
        super().__init__()

    def put(self, key, item):
        ''' add item into the cache '''
        if key in self.cache_data:
            self.luf[key] += 1
            self.cache_data[key] = item
        else:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                temp = float('inf')
                less_used = ''
                for k, v in self.luf.items():
                    if v < temp:
                        temp = v
                        less_used = k

                del self.luf[less_used]
                del self.cache_data[less_used]

            if key in self.luf:
                self.luf[key] += 1
            else:
                self.luf[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        ''' get the value of a key from the cache '''
        if key is not None and key in self.cache_data:
            self.luf[key] += 1
            return self.cache_data[key]
        return None
