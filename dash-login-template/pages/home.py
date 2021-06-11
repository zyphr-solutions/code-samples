"""
Define page attributes, layout and callbacks.
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import request

from app import app
from utils.components import Header


TITLE = "Home"
PERMISSION = ["user", "admin"]


def get_content():
    session_cookie = request.cookies.get("custom-auth-session")
    return html.Div(
        children=[
            html.P(children=["Welcome ", html.B(session_cookie), "!"]),
            html.P(
                children=[
                    "See what pages, under the ",
                    html.B("Apps"),
                    " navbar dropdown, are available to you according to your group permission.",
                ]
            ),
        ]
    )


def layout(url_args=None):
    return dbc.Container(children=[Header(TITLE), get_content()], className="mt-5")
