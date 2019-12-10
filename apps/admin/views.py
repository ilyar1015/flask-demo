from apps.admin import admin


@admin.route("/")
def index():
    return "没有后台"
