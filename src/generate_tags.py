"""
Generates tag files under 'tags/' for each tag in a post. Run manually before deployment.
Original: https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py
"""

import glob
import os

dir_posts, dir_tags = "_posts/", "tags/"

# Tag stuff
tag_identifier = "tags: "
tag_remove_chars = [tag_identifier, '[', ']', '\n']

tags, filenames = set(), glob.glob(dir_posts + '*md')
for filename in filenames:
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(tag_identifier):
                for char in tag_remove_chars:
                    line = line.replace(char, '')
                clean_tags = line.split(',')
                for tag in clean_tags:
                    tags.add(tag.strip())
                break

print("Found tags:", ", ".join(tags))

new_files = set()
old_files = set([tag.replace('\\', '/') for tag in glob.glob(dir_tags + '*.md')])
for tag in old_files:
    os.remove(tag)

if not os.path.exists(dir_tags):
    os.makedirs(dir_tags)

for tag in tags:
    tag_filename = dir_tags + tag + '.md'
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

message = "Updated %s, added %s, and deleted %s tag files." % (updated_file_count, new_file_count, old_file_count)
print(message)
