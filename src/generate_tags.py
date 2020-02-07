"""
Generates tag files under 'tags/' for each tag in a post. Run manually before deployment.
Original: https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py
"""

import glob
import os
from typing import Set

DIR_POSTS, DIR_TAGS = "_posts/", "tags/"
_TAG_IDENTIFIER = "tags: "

def find_tags() -> Set[str]:
    tag_remove_chars = [_TAG_IDENTIFIER, '[', ']', '\n']

    tags, filenames = set(), glob.glob(DIR_POSTS + '*md')
    for filename in filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith(_TAG_IDENTIFIER):
                    for char in tag_remove_chars:
                        line = line.replace(char, '')
                    clean_tags = line.split(',')
                    for tag in clean_tags:
                        tags.add(tag.strip())
                    break
    return tags

def find_tag_files() -> Set[str]:
    return set([tag.replace('\\', '/') for tag in glob.glob(DIR_TAGS + '*.md')])


if __name__ == "__main__":
    tags = find_tags()
    print("Found tags:", ", ".join(tags))

    new_files = set()
    old_files = find_tag_files()

    # Remove existing tag files and ensure tag folder existing
    [os.remove(tag) for tag in old_files]
    if not os.path.exists(DIR_TAGS):
        os.makedirs(DIR_TAGS)

    # Generate new tags
    for tag in tags:
        tag_filename = DIR_TAGS + tag + '.md'
        new_files.add(tag_filename)
        with open(tag_filename, 'a') as f:
            f.writelines([
                "---\n",
                "layout: tags\n",
                "title: \"Tag: %s\"\n" % tag,
                "tag: \"%s\"\n" % tag,
                "---\n"
            ])

    updated_file_count = len(new_files.intersection(old_files))
    old_file_count = len(old_files.difference(new_files))
    new_file_count = len(new_files.difference(old_files))

    print(f"Updated {updated_file_count}, added {new_file_count}, and deleted {old_file_count} tag files.")
