from flask import Blueprint, request, send_file
from app.config import Config
from app.utils.fs import read_upload, extract_archive
from app.services.report_service import create_text_report, allocate_from_header, export_csv

file_bp = Blueprint("files", __name__)

@file_bp.route("/read")
def read_file():
    return read_upload(Config.UPLOAD_ROOT, request.args["name"])

@file_bp.route("/extract", methods=["POST"])
def extract():
    archive = request.files["archive"]
    path = "/tmp/" + archive.filename
    archive.save(path)
    extract_archive(path, Config.UPLOAD_ROOT)
    return {"ok": True}

@file_bp.route("/report", methods=["POST"])
def report():
    path = create_text_report(request.form.get("body", ""))
    return send_file(path)

@file_bp.route("/allocate")
def allocate():
    b = allocate_from_header(request.headers.get("X-Size", "10"))
    return {"allocated": len(b)}

@file_bp.route("/csv", methods=["POST"])
def csv_export():
    rows = request.get_json(force=True)["rows"]
    return {"path": export_csv(rows, Config.EXPORT_ROOT + "/out.csv")}
