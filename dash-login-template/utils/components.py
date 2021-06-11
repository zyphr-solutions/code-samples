"""
Define reusable components. 
"""

import dash_bootstrap_components as dbc
import dash_html_components as html


def Header(title):
    """
    Construct a header with the given title.
    """
    return html.Div(
        style={"marginBottom": 0},
        children=[html.H1(style={"fontSize": 30}, children=title), html.Br()],
    )


def Navbar(app_logo, app_title, navbar_content=None):
    """
    Construct a navbar with the given app logo, app title and navbar dropdown content.
    """
    return dbc.Navbar(
        dbc.Container(
            children=[
                html.A(
                    dbc.Row(
                        children=[
                            dbc.Col(html.Img(src=app_logo, height="40px")),
                            dbc.Col(dbc.NavbarBrand(app_title, className="ml-2")),
                        ],
                        align="center",
                        no_gutters=True,
                    ),
                    href="/",
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(navbar_content, className="ml-auto", navbar=True),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ]
        ),
        color="light",
        light=True,
        className="mb-5",
        style=({"display": "flex"} if navbar_content else {"display": "none"}),
    )
