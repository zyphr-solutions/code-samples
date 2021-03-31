"""
Define helper methods.
"""

import os
import glob


def get_pages(directory, group=None):
    """
    Get a list of Python file paths in the given (nested) directory. Convert each
    file path into a url path to note page location within the app, and a module path
    to import the module containing the page layout.
    e.g. 'pages/page.py' -> '/page' and 'pages.page'
    e.g. 'pages/dir/page.py' -> '/dir/page' and 'pages.dir.page'
    Return a dictionary of pages, with the url path as key and the module as value.

    If user group specified, only include pages with permissions matching user group.
    Permissions are noted as a constant in each module. Otherwise, include all pages.

    This function will be used to populate the navbar with page links and to access
    page layouts. Note that this list does not account for urls that do not have a
    layout specified in a Python file within the given directory (e.g. '/logout').
    """
    pages = {}
    path_pattern = os.path.join(directory, "**", "*.py")
    paths = glob.glob(path_pattern, recursive=True)
    for path in paths:
        if not path.endswith("__init__.py"):
            path = "".join(path.split(".")[:-1])
            url_path = "/".join([""] + path.split("/")[1:])
            module_path = path.replace("/", ".")
            module = __import__(module_path, fromlist=[None])
            if group:
                if group in module.PERMISSION:
                    pages[url_path] = module
            else:
                pages[url_path] = module
    for page in pages:
        print(page)
    return pages
