from add_extension import add_extension
from add_extension_rec import add_extension_rec
from rm_extension import rm_extension
from rm_extension_rec import rm_extension_rec

import unittest
import os
import shutil

class TestUtiltyFunctions(unittest.TestCase):
    def setUp(self):
        # Remove old temp directory
        if os.path.exists(os.path.join(os.getcwd(), "temp")):
            shutil.rmtree("temp")

        # Make a temp directory
        os.mkdir("temp")
        os.mkdir("temp/temp")

        # Make a number of temporary files
        file1 = open("temp/file1.txt", "w+")
        file1.close()

        file2 = open("temp/file2.py", "w+")
        file2.close()

        file3 = open("temp/temp/file3.txt", "w+")
        file3.close()

        file4 = open("temp/temp/file4.py", "w+")
        file4.close()

    def tearDown(self):
        # Remove temp directory and all files
        shutil.rmtree("temp")

    def test_add_extension(self):
        prev_count = count_files_with_extension("temp", ".txt", False)
        prev_count_rec = count_files_with_extension("temp", ".txt", True)
        self.assertEqual(prev_count, 1)
        self.assertEqual(prev_count_rec, 2)

        # Run the add extension
        add_extension(".txt", "temp", True)

        count = count_files_with_extension("temp", ".txt", False)
        count_rec = count_files_with_extension("temp", ".txt", True)
        self.assertEqual(count, 2)
        self.assertEqual(count_rec, 3)

    def test_add_extension_rec(self):
        prev_count = count_files_with_extension("temp", ".txt", False)
        prev_count_rec = count_files_with_extension("temp", ".txt", True)
        self.assertEqual(prev_count, 1)
        self.assertEqual(prev_count_rec, 2)

        # Run the add extension
        add_extension_rec(".txt", "temp", True)

        count = count_files_with_extension("temp", ".txt", False)
        count_rec = count_files_with_extension("temp", ".txt", True)
        self.assertEqual(count, 2)
        self.assertEqual(count_rec, 4)

def count_files_with_extension(dir, ext, rec = True):
        """ Helper function to count all files in directory with extension

        Args:
            dir: Directory to search in
            ext: Extension to search for
            rec: Whether or not the search is recursive

        Returns:
            Count of the files matching the extension
        """
        cnt = 0
        if rec:
            for (_, _, filenames) in os.walk(dir):
                for filename in filenames:
                    if filename.endswith(ext):
                        cnt += 1
        else:
            for filename in os.listdir(dir):
                if not os.path.isfile(os.path.join(dir, filename)):
                    continue
                if filename.endswith(ext):
                    cnt += 1
        return cnt

if __name__=="__main__":
    unittest.main()
