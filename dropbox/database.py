import time
class InmemoryDataBase:
    def __init__(self):
        self.db = {}
    
    def insert(self, key, value):
        self.db[key] = value
    
    def retrieve(self, key):
        return self.db.get(key, None)

    def delete(self, key):
        if key in self.db:
            del self.db[key]
        

class InMememoryDataBaseWithTTL(InmemoryDataBase):
    def __init__(self):
        super().__init__()
        self.ttl = {}
    
    def insert(self, key, value, ttl=None):
        super().insert(key, value)
        if ttl:
            self.ttl[key] = time.time() + ttl
        
    def retrieve(self, key):
        if self.ttl[key] > time.time():
            super().delete(key)
            del self.ttl[key]
            return None
        
        return super().retrieve(key)

    def delete(self, key):
        super().delete(key)
        if key in self.ttl:
            del self.ttl[key]

class InMemoryDataBaseWithIndexes(InMememoryDataBaseWithTTL):
    def __init__(self):
        super().__init__()
        self.index = {}
    
    def insert(self, key, value: dict):
        super().insert()

        for field, filed_value in value.items():
            if field not in self.index:
                self.index[field] = {}
            self.index[field].setdefault(filed_value, []).append(key)

    def query_by_index(self, field, value):
        return self.index.get(field, {}).get(value, [])

class InMemoryDataBaseWithTransactions(InMemoryDataBaseWithIndexes):
    def __init__(self):
        super().__init__()
        self.transactions_stack = []
    
    def begin(self):
        self.transactions_stack.append((self.db, self.index))
    
    def roll_back(self):
        if self.transactions_stack:
            self.db, self.index = self.transactions_stack.pop()
        
        else:
            return "No active transaction to commit."
    
    def commit(self):
        if self.transactions_stack:
            self.transactions_stack.pop()
        
        else:
            return "No active transaction to rollback."