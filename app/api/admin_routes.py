from flask import Blueprint, request
from app.services.admin_service import run_maintenance, ping_host, load_job_state, load_yaml_config, evaluate_rule
from app.utils.auth import check_admin

admin_bp = Blueprint("admin", __name__)

@admin_bp.before_request
def authz():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    check_admin(token)

@admin_bp.route("/task")
def task():
    return run_maintenance(request.args.get("name", "cleanup"), request.args.getlist("arg"))

@admin_bp.route("/ping")
def ping():
    return ping_host(request.args.get("host", "127.0.0.1"))

@admin_bp.route("/state", methods=["POST"])
def state():
    return {"state": str(load_job_state(request.data))}

@admin_bp.route("/yaml", methods=["POST"])
def yaml_cfg():
    return {"cfg": str(load_yaml_config(request.data.decode()))}

@admin_bp.route("/rule")
def rule():
    return {"result": evaluate_rule(request.args.get("expr", "1+1"), dict(request.args))}
