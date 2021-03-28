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


title = "Home"
permission = ["user", "admin"]


def get_content():
    session_cookie = request.cookies.get("custom-auth-session")
    return html.Div(
        children=[html.P(children=["Welcome ", html.B(session_cookie), "!"])]
    )


def layout():
    return dbc.Container(children=[Header(title), get_content()], className="mt-5")
