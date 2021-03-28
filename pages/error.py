"""
Define page attributes, layout and callbacks.
"""

import dash_bootstrap_components as dbc
import dash_html_components as html

from utils.components import Header


title = "Error 404"
permission = ["user", "admin"]
show_on_navbar = True


def layout():
    return dbc.Container(
        children=[
            Header(title),
            html.P("Page not found"),
        ],
        className="mt-5",
    )
