"""
Configure Flask Blueprint for user authentication.
"""

from flask import Blueprint, request, redirect

from app import bcrypt
from utils.constants import URL
from data.users import USERS

auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route(URL["login"], methods=["POST"])
def route_login():
    """
    Login user once login form submitted.
    """
    username = request.form.get("login-username")
    password = request.form.get("login-password")
    if username or password:
        if username in USERS.keys() and bcrypt.check_password_hash(
            USERS[username]["password"], password
        ):
            print("LOGIN:", username)
            rep = redirect(URL["home"])
            rep.set_cookie("custom-auth-session", username)
        else:
            rep = redirect(f"{URL['login']}?error=invalid")
    else:
        rep = redirect(f"{URL['login']}?error=incomplete")
    return rep


@auth_blueprint.route(URL["logout"], methods=["POST"])
def route_logout():
    """
    Logout user once logout form submitted.
    """
    rep = redirect(URL["login"])
    rep.set_cookie("custom-auth-session", "", expires=0)
    return rep
