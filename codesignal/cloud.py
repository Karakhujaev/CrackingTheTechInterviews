import zlib
import base64

class CloudFileSystemImpl:
    def __init__(self):
        self.storage = {}

    def create_file(self, name: str, size: int, content: str) -> bool:
        if name in self.storage:
            return False

        self.storage[name] = {
            "content": self.compress_content(content),
            "size": size
        }
        return True
    
    def read_file(self, name: str) -> bool:
        if name not in self.storage:
            raise ValueError(f"There is no file with name: {name}")

        return f"File name: {name}, Size: {self.storage[name]["size"]} Content: {self.decompress_content(self.storage[name]["content"])}"

    
    def delete_file(self, name: str) -> bool:
        if name not in self.storage:
            raise ValueError(f"There is no file with name: {name}")

        del self.storage[name]
        return True


    def copy_file(self, from_name: str, to_name: str) -> int:
        if from_name not in self.storage:
            raise ValueError(f"There is no file with name: {from_name}")

        if to_name in self.storage:
            raise ValueError(f"File with name:{to_name} already exists: {from_name}")

        self.storage[to_name]  = {
            "content": self.compress_content(self.compress_content(self.storage[from_name]["content"])),
            "size": self.storage[from_name]["size"]
        }
        return True

    def search(self, prefix: str, suffix: str) -> list:
        result = []
        for name, meta_data in self.storage.items():
            if name.startswith(prefix) and name.endswith(suffix):
                result.append(f"{name}({meta_data["size"]})")
        
        return result

    @classmethod
    def compress_content(self, content: str):
        compressed = zlib.compress(content.encode())
        return base64.b64encode(compressed).decode()

    @classmethod
    def decompress_content(self, content: str):
        compressed = base64.b64decode(content.encode())
        return zlib.decompress(compressed).decode()