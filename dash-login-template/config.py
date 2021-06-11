"""
Config for Flash server.
"""

import os
import sys

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    """
    Flask server configuration variables.
    """

    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise Exception("SECRET_KEY is not defined in your environment.")
    if sys.version_info[0] >= 3:
        SECRET_KEY = SECRET_KEY.encode("utf8")
