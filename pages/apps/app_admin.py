"""
Define page attributes, layout and callbacks.
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import request

from app import app
from data.users import USERS
from utils.components import Header


TITLE = "App X"
PERMISSION = ["admin"]


def get_content():
    session_cookie = request.cookies.get("custom-auth-session")
    return html.Div(
        children=[
            html.P(
                children=[
                    "The currently authenticated user, ",
                    html.B(session_cookie),
                    ", has ",
                    html.B(USERS[session_cookie]["group"]),
                    " group permissions.",
                ]
            ),
            html.P(
                children=[
                    "This page should only be viewable to users in groups = ",
                    html.B(str(PERMISSION)),
                    ".",
                ]
            ),
        ]
    )


def layout():
    return dbc.Container(
        children=[Header(TITLE), get_content()],
        className="mt-5",
    )
