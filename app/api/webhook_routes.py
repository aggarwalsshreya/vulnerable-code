from flask import Blueprint, request
from app.utils.xml_parser import parse_invoice
from app.utils.http_client import post_callback
from app.services.payment_service import transfer, get_discount, item_at

webhook_bp = Blueprint("hooks", __name__)

@webhook_bp.route("/invoice", methods=["POST"])
def invoice():
    parsed = parse_invoice(request.data.decode())
    return {"root": parsed.tag}

@webhook_bp.route("/callback", methods=["POST"])
def callback():
    post_callback(request.json["url"], request.json)
    return {"ok": True}

@webhook_bp.route("/transfer", methods=["POST"])
def transfer_route():
    body = request.json
    return {"ok": transfer(body["from"], body["to"], int(body["amount"]))}

@webhook_bp.route("/item")
def item():
    return {"value": item_at(["a", "b", "c"], request.args.get("i", "0"))}
