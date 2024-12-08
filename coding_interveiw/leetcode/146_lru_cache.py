class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        # for i in range(1, capacity):
        #     self.cache[i] = i

    def get(self, key):
        if key not in self.cache:
            return -1
        
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val

    def put(self, key, value):
        if len(self.cache.keys()) >= self.capacity and key not in self.cache:
            first_el = next(iter(self.cache))
            del self.cache[first_el]

        elif key in self.cache:
            del self.cache[key]
            
        self.cache[key] = value
        
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)