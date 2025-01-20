import os
import hashlib
import tempfile

def find_duplicate_files(folder_path):
    def get_file_hash(file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):  
                hasher.update(chunk)
        return hasher.hexdigest()

    size_map = {}  
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            size_map.setdefault(file_size, []).append(file_path)

    for files in size_map.values():
        if len(files) > 1:  
            hash_map = {}
            for file_path in files:
                file_hash = get_file_hash(file_path)
                hash_map.setdefault(file_hash, []).append(file_path)
            
            # Collect duplicates
            for file_list in hash_map.values():
                if len(file_list) > 1:
                    duplicates.extend(file_list)

    return duplicates

def create_test_environment():
    temp_dir = tempfile.mkdtemp()
    
    file1 = os.path.join(temp_dir, "file1.txt")
    file2 = os.path.join(temp_dir, "file2.txt")
    file3 = os.path.join(temp_dir, "file3.txt")
    file4 = os.path.join(temp_dir, "subfolder", "file4.txt")

    os.mkdir(os.path.join(temp_dir, "subfolder"))

    with open(file1, "w") as f:
        f.write("duplicate content")
    with open(file2, "w") as f:
        f.write("duplicate content")
    with open(file3, "w") as f:
        f.write("unique content")
    with open(file4, "w") as f:
        f.write("duplicate content")

    return temp_dir



import unittest

class TestFindDuplicates(unittest.TestCase):
    def test_regular_case(self):
        temp_dir = create_test_environment()
        self.assertEqual(len(find_duplicate_files(temp_dir)), 3)


if __name__ == "__main__":
    unittest.main()