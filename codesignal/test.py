import unittest
from cloud import CloudFileSystemImpl

class TestCloudFileSystemImpl(unittest.TestCase):
    
    def setUp(self):
        """Create a CloudFileSystemImpl instance before each test."""
        self.cloud_fs = CloudFileSystemImpl()

    def test_create_file_success(self):
        """Test that creating a file with a unique name is successful."""
        result = self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        self.assertTrue(result)
        self.assertIn("file1.txt", self.cloud_fs.storage)

    def test_create_file_fail_existing_file(self):
        """Test that creating a file with an existing name fails."""
        self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        result = self.cloud_fs.create_file("file1.txt", 100, "New content")
        self.assertFalse(result)

    def test_read_file_success(self):
        """Test reading a file that exists."""
        self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        content = self.cloud_fs.read_file("file1.txt")
        self.assertIn("file1.txt", content)
        self.assertIn("Hello, World!", content)

    def test_read_file_fail_not_found(self):
        """Test reading a file that doesn't exist."""
        with self.assertRaises(ValueError):
            self.cloud_fs.read_file("file2.txt")

    def test_delete_file_success(self):
        """Test that deleting a file works."""
        self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        result = self.cloud_fs.delete_file("file1.txt")
        self.assertTrue(result)
        self.assertNotIn("file1.txt", self.cloud_fs.storage)

    def test_delete_file_fail_not_found(self):
        """Test deleting a file that doesn't exist."""
        with self.assertRaises(ValueError):
            self.cloud_fs.delete_file("file2.txt")

    def test_copy_file_success(self):
        """Test copying an existing file to a new name."""
        self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        result = self.cloud_fs.copy_file("file1.txt", "file2.txt")
        self.assertTrue(result)
        self.assertIn("file2.txt", self.cloud_fs.storage)

    def test_copy_file_fail_source_not_found(self):
        """Test copying a file that doesn't exist."""
        with self.assertRaises(ValueError):
            self.cloud_fs.copy_file("file3.txt", "file4.txt")

    def test_copy_file_fail_target_exists(self):
        """Test copying a file when the target file already exists."""
        self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        self.cloud_fs.create_file("file2.txt", 100, "New content")
        with self.assertRaises(ValueError):
            self.cloud_fs.copy_file("file1.txt", "file2.txt")

    def test_search_success(self):
        """Test searching for files based on prefix and suffix."""
        self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        self.cloud_fs.create_file("file2.txt", 200, "New content")
        result = self.cloud_fs.search("file", "txt")
        self.assertEqual(result, ["file1.txt(100)", "file2.txt(200)"])

    def test_search_no_results(self):
        """Test searching when no files match the criteria."""
        self.cloud_fs.create_file("file1.txt", 100, "Hello, World!")
        result = self.cloud_fs.search("file", "pdf")
        self.assertEqual(result, [])

    def test_compress_decompress(self):
        """Test the compression and decompression of content."""
        original_content = "Hello, World!"
        compressed = self.cloud_fs.compress_content(original_content)
        decompressed = self.cloud_fs.decompress_content(compressed)
        self.assertEqual(original_content, decompressed)

if __name__ == "__main__":
    unittest.main()
