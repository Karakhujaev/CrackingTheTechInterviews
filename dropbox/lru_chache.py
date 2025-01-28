from collections import OrderedDict

class LruCache:
    def __ini__(self, capacity=3):
        self.data = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        result = self.data.get(key, None)
        if result:
            self.data.move_to_end(key)

        return result
    
    def put(self, key, data):
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
        
        self.data[key] = data
        self.data.move_to_end(key)
        return self.data[key]
