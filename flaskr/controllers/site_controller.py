from flask import Blueprint, render_template, flash

site_bp = Blueprint("site", __name__, url_prefix="/")

@site_bp.route("/", methods=["GET"])
def index():
    return render_template("dashboard/dashboard.html")


    