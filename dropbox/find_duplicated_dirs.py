import os
import tempfile
import unittest

def find_duplicated_directories(path):
    directories = {}
    duplicated_directories = []
    for root, sub_directories, _ in os.walk(path):
        for sub_directory in sub_directories:
            if sub_directory not in directories:
                directories[sub_directory] = 0
            
            directories[sub_directory] += 1
    
    for key, val in directories.items():
        if val > 1:
            duplicated_directories.append(key)


def create_test_enviriment():
    temp_dir = tempfile.mkdtemp()

    os.mkdir(os.path.join(temp_dir, "duplicated"))
    file1 = os.path.join(temp_dir, "duplicated", "hello.txt")
    os.mkdir(os.path.join(temp_dir, "duplicated", "duplicated"))
    os.mkdir(os.path.join(temp_dir, "unique"))
    os.mkdir(os.path.join(temp_dir, "unique", "duplicated"))

    with open(file1, "w") as f1:
        f1.write("Hello World!")
    
    return temp_dir

print(create_test_enviriment())
class TestFindDuplicates(unittest.TestCase):
    def test_regular_case(self):
        temp_dir = create_test_enviriment()
        # self.assertEqual(len(find_duplicated_directories(temp_dir)), 1)


if __name__ == "__main__":
    unittest.main()