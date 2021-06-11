"""
Define global constants. 
"""

import os

import dash_bootstrap_components as dbc

APP_TITLE = "Zyphr"
APP_LOGO = os.path.join("assets", "logo-profile.png")
APP_CSS = [dbc.themes.MINTY]

TOGGLE = {
    "create_account": True,
    "forgot_password": True,
}

PATH = {
    "pages": os.path.join("pages"),
}

URL = {
    "home": "/home",
    "login": "/login",
    "logout": "/logout",
    "error": "/error",
}
