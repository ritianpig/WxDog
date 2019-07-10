from flask import Blueprint, url_for
from flask import redirect


rejump = Blueprint("rejump", __name__)

@rejump.route("/rejump", methods=["GET", "POST"])
def jump():
    return redirect("https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4MDg4ODc5OQ==&scene=126&bizpsid=0#wechat_redirect")

@rejump.route("/rejump2", methods=["GET", "POST"])
def jump2():
    return redirect("https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx08ba15ad70bb3e53&redirect_uri=https%3a%2f%2fdog.minifmsd.cn%2foauth_cash_p&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect")

@rejump.route("/rejump_x1", methods=["GET", "POST"])
def jump3():
    return redirect("https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4MDg4ODc5OQ==&scene=126&bizpsid=0#wechat_redirect")

@rejump.route("/rejump_x2", methods=["GET", "POST"])
def jump4():
    return redirect("https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4MDg4ODc5OQ==&scene=126&bizpsid=0#wechat_redirect")

@rejump.route("/rejump_x3", methods=["GET", "POST"])
def jump5():
    return redirect("https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4MDg4ODc5OQ==&scene=126&bizpsid=0#wechat_redirect")

@rejump.route("/rejump_x4", methods=["GET", "POST"])
def jump6():
    return redirect("https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4MDg4ODc5OQ==&scene=126&bizpsid=0#wechat_redirect")

@rejump.route("/rejump_f", methods=["GET", "POST"])
def jump7():
    return redirect("https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4MDg4ODc5OQ==&scene=126&bizpsid=0#wechat_redirect")
