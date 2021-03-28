"""
Define empty page for routing.
"""

import dash_html_components as html


title = "Home"
permission = ["user", "admin"]


def layout():
    return html.Div()
