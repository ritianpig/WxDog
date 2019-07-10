from datetime import datetime

from WxDog.extensions import db
from flask_login import UserMixin


class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ebook_id = db.Column(db.String(20), unique=True, comment="电子书序号")
    classification = db.Column(db.String(200), default="", comment="所属分类")
    ebook_title = db.Column(db.String(100), default="", comment="电子书标题")
    introduce = db.Column(db.String(500), default="", comment="简介")
    envelope_url = db.Column(db.String(255), default="", comment="封皮地址")
    ebook_price = db.Column(db.String(10), default="0", comment="价格")
    total_chapter = db.Column(db.String(10), default="0", comment="总章数")
    is_pay = db.Column(db.String(5), default="1", comment="是否付费")
    free_trials = db.Column(db.String(10), default="0", comment="免费试读章节数")


class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.String(20), comment="章序号")
    ebook_id = db.Column(db.String(20), comment="电子书序号")
    chapter_title = db.Column(db.String(100), default="", comment="章标题")
    chapter_price = db.Column(db.String(10), default="0", comment="章价格")
    is_pay = db.Column(db.String(5), default="1", comment="是否付费")
    is_trials = db.Column(db.String(5), default="0", comment="是否为试读")


class Article(db.Model):
    article_id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.String(20), comment="章序号")
    ebook_id = db.Column(db.String(20), comment="电子书序号")
    is_update = db.Column(db.String(5), default="1", comment="是否更新中")
    article_title = db.Column(db.String(100), default="", comment="标题")
    content = db.Column(db.TEXT, default="", comment="文章内容")
    article_price = db.Column(db.String(10), default="0", comment="节价格")
    is_pay = db.Column(db.String(5), default="1", comment="是否付费")
    is_trials = db.Column(db.String(5), default="0", comment="是否为试读")
    pic_url = db.Column(db.String(200), default="", comment="图片地址")
    enter_date = db.Column(db.DateTime, comment="录入时间")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    other_name = db.Column(db.String(100), comment="用户昵称")
    openid = db.Column(db.String(200), comment="用户openid")
    unionid = db.Column(db.String(200), comment="unionid")
    sex = db.Column(db.String(5), comment="性别")
    age = db.Column(db.String(3), comment="年龄")
    area = db.Column(db.String(100), comment="区域")
    income = db.Column(db.String(10), comment="收入")
    want_buy = db.Column(db.String(50), comment="购买意向")
    telnum = db.Column(db.String(11), comment="电话号码")
    typephone = db.Column(db.String(50), comment="手机型号")
    grade_vip = db.Column(db.String(10), comment="vip等级")
    add_date = db.Column(db.DateTime, comment="用户入库时间")


class Vip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), comment="vip名称")
    grade = db.Column(db.String(10), comment="等级")
    introduce = db.Column(db.TEXT, comment="vip描述")
    price = db.Column(db.String(10), comment="vip价格")


class VipOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(200), comment="用户openid")
    unionid = db.Column(db.String(200), comment="unionid")
    grade = db.Column(db.String(10), comment="等级")
    buy_date = db.Column(db.DateTime, comment="购买时间")
    lose_date = db.Column(db.DateTime, comment="到期时间")


class UserBuys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(200), comment="用户openid")
    ebook_id = db.Column(db.Integer, comment="电子书序号")
    buydate = db.Column(db.DateTime, comment="购买时间")


class AdminLogin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(128))