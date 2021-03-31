"""
Define empty page for routing.
"""

import dash_html_components as html


TITLE = "Home"
PERMISSION = ["user", "admin"]


def layout():
    return html.Div()
