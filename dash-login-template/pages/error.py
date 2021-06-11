"""
Define page attributes, layout and callbacks.
"""

import dash_bootstrap_components as dbc
import dash_html_components as html

from utils.components import Header


TITLE = "Error 404"
PERMISSION = ["user", "admin"]


def layout(url_args=None):
    return dbc.Container(
        children=[
            Header(TITLE),
            html.P("Page not found"),
        ],
        className="mt-5",
    )
