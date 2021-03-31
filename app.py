"""
Configure Dash app and Flask server. Define plugins and bind to Flask server. 
"""

import dash
from flask_bcrypt import Bcrypt

from utils.constants import APP_CSS


app = dash.Dash(
    __name__, external_stylesheets=APP_CSS, suppress_callback_exceptions=True
)
server = app.server
server.config.from_object("config.Config")

bcrypt = Bcrypt(server)

with server.app_context():
    from auth import auth_blueprint

    server.register_blueprint(auth_blueprint)
