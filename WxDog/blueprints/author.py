import os

from flask import Blueprint, request, render_template, redirect, url_for, flash
from WxDog.forms import LoginForm
from WxDog.models import AdminLogin
from flask_login import login_user, current_user, login_required, logout_user


author = Blueprint("author", __name__)


def redirect_back(default='author.login', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        else:
            return redirect(target)
    return redirect(url_for(default, **kwargs))


@author.route("/a")
@login_required
def a():
    if current_user.is_active:
        return "ok"
    else:
        return redirect(url_for("login"))


@author.route('/tables', methods=["GET", "POST"])
@login_required
def tables():
    return render_template("table.html")


@author.context_processor
def title():
    key = ["Login", "训狗电子书", "Chapter", "Article", "Loginout"]
    return dict(key=key)


@author.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        # if current_user.is_authenticated:
        #     return redirect_back()
        # else:
        return render_template("login.html", form=form)
    else:
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            remember = form.remember.data
            admin = AdminLogin.query.first()
            if admin:
                if username == admin.username and password == admin.password:
                    login_user(admin, remember)
                    flash("登录成功")
                    return redirect(url_for("author.admin"))
                else:
                    flash("用户名或密码无效")
            else:
                flash("请开通登录权限")
        return render_template("login.html", form=form)


@author.route("/admin")
def admin():
    return render_template("base.html")


#
#

#
# @author.route("/logout")
# def logout():
#     logout_user()
#     return "注销成功"
