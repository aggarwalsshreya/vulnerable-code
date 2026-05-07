from flask import Blueprint, request, Response, redirect, make_response
from app.services.user_service import lookup_user, notes_for_user, change_profile, reset_password
from app.utils.rendering import unsafe_html, render_custom_template
from app.utils.auth import make_session_cookie
from app.utils.http_client import fetch_user_url
from app.utils.logging_utils import audit

user_bp = Blueprint("users", __name__)

@user_bp.route("/search")
def search():
    audit("search", request.args.get("q", "anonymous"))
    return {"rows": str(lookup_user(request.args))}

@user_bp.route("/<user_id>/notes")
def notes(user_id):
    return {"notes": str(notes_for_user(user_id, request.args.get("term", "")))}

@user_bp.route("/<user_id>/profile", methods=["POST"])
def profile(user_id):
    change_profile(user_id, request.get_json(force=True))
    return {"ok": True}

@user_bp.route("/hello")
def hello():
    return Response(unsafe_html(request.args.get("name", "guest")), mimetype="text/html")

@user_bp.route("/template", methods=["POST"])
def template():
    return render_custom_template(request.form["template"], dict(request.form))

@user_bp.route("/avatar")
def avatar_proxy():
    return fetch_user_url(request.args["url"])

@user_bp.route("/redirect")
def go():
    return redirect(request.args.get("next", "/"))  # CWE-601

@user_bp.route("/login")
def login():
    resp = make_response({"logged_in": True})
    return make_session_cookie(resp, request.args.get("sid", "guest"))

@user_bp.route("/reset")
def reset():
    reset_password(request.args.get("id", "1"), request.args.get("callback"))
    return {"sent": True}
