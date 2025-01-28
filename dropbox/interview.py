class InMemoryDBImpl:

    def __init__(self):
        self.db = {}
        self.ttl_db = {}
        self.index = {}
    
    def set_with_ttl(self, timestamp: int, key: str, field: str, value: int, ttl):
        if key not in self.db:
            self.db[key] = {}
        
        self.db[key][field] = value
        if key not in self.ttl_db:
            self.ttl_db[key] = {}
            
        self.ttl_db[key][field] = timestamp + ttl
    
    def compare_and_set_with_ttl(self, timestamp: int, key: str, field: str, expected_value: int, new_value: int, ttl: int) -> bool:
        if key in self.db and field in self.db[key]:
            current_value = self.db[key]
            if current_value == expected_value:
                self.db[key][field] = new_value
                self.ttl_db[key][field] = timestamp + ttl
                return True
        return False

    # TODO: implement interface methods here
    def set(self, timestamp: int, key: str, field: str, value: int) -> None:
        if key not in self.db:
            self.db[key] = {}
    
        if field not in self.index:
            self.index.setdefault(field, {})
        
        if value not in self.index[field]:
            self.index[field].setdefault(value, [])
            
        self.index[field][value].append(key)
        self.db[key][field] = value

    def compare_and_set(self, timestamp: int, key: str, field: str, expected_value: int, new_value: int) -> bool:
        if key not in self.db:
            return False
        
        if field not in self.db[key]:
            return False
        
        if expected_value != self.db[key][field]:
            return False
        
        self.db[key][field] = new_value
        return True

    def compare_and_delete(self, timestamp: int, key: str, field: str, expected_value: int) -> bool:
        if key not in self.db:
            return False
        
        if field not in self.db[key]:
            return False
        
        if self.db[key][field] != expected_value:
            return False
        
        del self.db[key][field]
        return True
            
        
    def get(self, timestamp: int, key: str, field: str) -> int | None:
        if key not in self.db:
            return None
        
        if field not in self.db[key]:
            return None
        
        if type(self.db[key][field]) == int:
            return self.db[key][field]
        
        if self.ttl_db[key][field] > timestamp:
            return self.db[key][field]
            
        return None
    
    def scan(self, timestamp: int, key: str) -> list[str]:
        if key not in self.db:
            return []
            
        result = sorted(self.db[key].items())
        return [f"{field}({value})" for field, value in result]
       
        
        
    def scan_by_prefix(self, timestamp: int, key: str, prefix: str):
        if key not in self.db:
            return []
            
        filtered_fields = {}
        for field, value in self.db[key].items():
            if str(field).startswith(prefix):
               filtered_fields[field] = value
        
        sorted_fields = sorted(filtered_fields.items())
        return [f"{field}({value})" for field, value in sorted_fields]