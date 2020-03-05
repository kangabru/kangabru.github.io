import unittest
from generate_tags import find_tags, find_tag_files
from os.path import basename


class TestTags(unittest.TestCase):
    def test_tags(self):
        tags = find_tags()
        tag_files = find_tag_files()

        len_tags, len_tag_files = len(tags), len(tag_files)
        self.assertEqual(len_tags, len_tag_files, f"The tab count ({len_tags}) for does not match the tab file count ({len_tag_files})")

        file_tags = set([basename(tag_file).replace('.md', '') for tag_file in tag_files])
        self.assertEqual(tags, file_tags)

if __name__ == "__main__":
    unittest.main()
