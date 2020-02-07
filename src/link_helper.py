from glob import glob
from re import compile, search
from urllib.request import urlopen, HTTPError


# Start with 'http' or 'www' up until a space, ", or )
_RE_URLS = compile(r'(?:http|www)(?:(?![\s\)"]).)*')


def get_files_from_pattern(glob_pattern):
    return glob(glob_pattern)


def get_links_from_file(file_path: str):
    urls = []
    with open(file_path) as f:
        content = "\n".join(f.readlines())
        urls = _RE_URLS.findall(content)
    return urls


def get_http_response(url: str):
    page, code = None, -1
    try:
        url_full = url if url.startswith('http') else f'http://{url}'
        page = urlopen(url_full)
        code = page.code
    except HTTPError as e:
        code = e.code
    except Exception as e:
        error = str(e.args)
        if 'uq.edu.au' in url and 'SSLCertVerificationError' in error:
            code = "SSL Error"
        else:
            print(f"Url {url} is not valid: {error}")
    finally:
        page and page.close()
    return code
