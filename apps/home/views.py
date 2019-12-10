from apps.home import home


@home.route("/")
def index():
    return "暂时没有首页"
