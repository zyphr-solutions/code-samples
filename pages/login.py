"""
Define page attributes, layout and callbacks.
"""

import dash_bootstrap_components as dbc
import dash_html_components as html

from data.users_unencrypted import USERS
from utils.components import Header
from utils.constants import APP_TITLE, APP_LOGO, URL


title = "Login"
permission = ["anon"]


def layout(args=None):
    error_message = ""
    error_display = False
    if args:
        if "error=incomplete" in args:
            error_message = "Please complete the form."
            error_display = True
        elif "error=invalid" in args:
            error_message = "Invalid username and password. Please try again."
            error_display = True

    creds = [dbc.ListGroupItem("Example (username, password) pairs:")]
    for username in USERS:
        user_creds = username + ": " + USERS[username]["password"]
        creds.append(dbc.ListGroupItem(user_creds, color="transparent"))

    return html.Div(
        id="login-page",
        children=[
            html.Div(
                html.Img(src=APP_LOGO, height="80px"),
            ),
            html.Div(
                Header("Log in to " + APP_TITLE),
            ),
            dbc.Card(
                id="login-card",
                children=[
                    dbc.CardBody(
                        html.Form(
                            id="login-form",
                            children=[
                                dbc.Alert(
                                    error_message,
                                    id="login-error-message",
                                    color="danger",
                                    dismissable=True,
                                    is_open=error_display,
                                ),
                                dbc.FormGroup(
                                    [
                                        dbc.Label(
                                            "Username", html_for="login-username"
                                        ),
                                        dbc.Input(
                                            id="login-username",
                                            name="login-username",
                                            type="text",
                                            n_submit=0,
                                        ),
                                    ]
                                ),
                                dbc.FormGroup(
                                    children=[
                                        dbc.Label(
                                            "Password", html_for="login-password"
                                        ),
                                        dbc.Input(
                                            id="login-password",
                                            name="login-password",
                                            type="password",
                                            n_submit=0,
                                        ),
                                    ]
                                ),
                                dbc.Button(
                                    "Login",
                                    id="login-button",
                                    type="submit",
                                    color="primary",
                                    block=True,
                                    n_clicks=0,
                                ),
                            ],
                            action=URL["login"],
                            method="POST",
                        )
                    ),
                ],
                color="light",
            ),
            dbc.ListGroup(creds, className="mt-3"),
        ],
    )
