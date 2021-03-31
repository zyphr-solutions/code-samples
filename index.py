"""
Define root app layout and callbacks. Run app server.
"""

import sys
import inspect

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import request

from app import app
from data.users import USERS
from utils.components import Navbar
from utils.constants import APP_TITLE, APP_LOGO, PATH, URL
from utils.helper import get_pages


def get_navbar():
    """
    Get navbar, content of which can change according to user authentication and
    group permissions.

    Currently, the navbar is hidden from unauthenticated users, but could also change
    to have the navbar show with limited links.
    """
    session_cookie = request.cookies.get("custom-auth-session")
    if session_cookie:
        if USERS[session_cookie]["group"] == "admin":
            dropdown_content = [
                dbc.DropdownMenuItem(dbc.NavLink("App X", href="/apps/app_admin")),
                dbc.DropdownMenuItem(dbc.NavLink("App Y", href="/apps/app_user")),
            ]
        else:
            dropdown_content = [
                dbc.DropdownMenuItem(dbc.NavLink("App Y", href="/apps/app_user")),
            ]
        navbar_content = [
            dbc.NavItem(dbc.NavLink("Home", href=URL["home"])),
            dbc.DropdownMenu(
                label="Apps",
                children=dropdown_content,
                nav=True,
                in_navbar=True,
                color="primary",
            ),
            html.Form(
                dbc.Button("Logout", type="submit", color="primary"),
                action=URL["logout"],
                method="POST",
                style={"padding-left": "1rem"},
            ),
        ]
    else:
        navbar_content = None
    return Navbar(APP_LOGO, APP_TITLE, navbar_content)


app.layout = html.Div(
    children=[dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname"), Input("url", "search")],
)
def display_page(url, args):
    """
    Define layout and redirect url according to input url and user authentication.

    Currently, if an authenticated user attempts to access a page that assumes no user
    is not logged in (e.g. login, register), they will be logged out before proceeding.
    This is applied when an authenticated user clicks the logout button and is redirected
    to the login page.

    If the user is not logged in, they are only permitted to access pages with "anon"
    group permissions (e.g. login), and if they attempt to access any other page,
    they will be redirected to the login page.

    If the user is logged in, they are only permitted to access pages with group permissions
    that match their user group on record, and if they attempt to access any other page,
    they will be redirected to the error page.

    The layout is accessed by the module path in the pages directory, matching its url path.
    """

    session_cookie = request.cookies.get("custom-auth-session")

    print("URL I:", url, session_cookie)

    if not session_cookie:
        PAGES = get_pages(PATH["pages"], "anon")
        if url not in PAGES:
            url = URL["login"]
    else:
        PAGES = get_pages(PATH["pages"], USERS[session_cookie]["group"])
        if url == "/":
            url = URL["home"]
        elif url not in PAGES:
            url = URL["error"]

    page = PAGES[url]

    navbar = get_navbar()
    layout_arg_spec = (
        inspect.getargspec(page.layout).args
        if sys.version_info[0] < 3
        else inspect.getfullargspec(page.layout).args
    )
    layout = page.layout(args) if "args" in layout_arg_spec else page.layout()

    print("URL O:", url, session_cookie)
    return [navbar, layout]


if __name__ == "__main__":
    app.run_server(debug=True)
