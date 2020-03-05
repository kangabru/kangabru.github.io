import unittest
from urllib.request import urlopen, HTTPError
from link_helper import get_files_from_pattern, get_links_from_file, get_http_response
from typing import Tuple


class TestLinks(unittest.TestCase):
    def test_links(self):
        failed_links: Tuple[str, str, int] = [] # [(<file path>, <url>, <code>), ...]
        iffy_links: Tuple[str, str, int] = [] # [(<file path>, <url>, <code>), ...]

        files = get_files_from_pattern('_posts/*.md')
        for file_path in files:
            links = get_links_from_file(file_path)
            for link in links:
                code = get_http_response(link)
                summary = (file_path, link, code)
                if code == 404 or code == -1: failed_links.append(summary)
                elif code != 200: iffy_links.append(summary)

        def links_summary(links):
            get_summary = lambda file_path, link, code: f"Url '{link}' in file '{file_path}' is not valid ({code})."
            return '\n'.join([get_summary(*summary) for summary in links])

        has_errors = len(iffy_links) + len(failed_links)
        if len(iffy_links):
            print("Manually check these links:")
            print(links_summary(iffy_links))

        if len(failed_links):
            self.fail(links_summary(failed_links))

        if not has_errors:
            print("All links look good")

if __name__ == "__main__":
    unittest.main()
