from WxDog.extensions import db


class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ebook_id = db.Column(db.String(50), unique=True, comment="电子书id")
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
    chapter_id = db.Column(db.String(50), comment="章id")
    chapter_title = db.Column(db.String(100), default="", comment="章标题")
    chapter_price = db.Column(db.String(10), default="0", comment="章价格")
    is_pay = db.Column(db.String(5), default="1", comment="是否付费")
    is_trials = db.Column(db.String(5), default="0", comment="是否为试读")
    ebook_id = db.Column(db.String(50), comment="电子书id")


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.String(50), comment="节id")
    is_update = db.Column(db.String(5), default="1", comment="是否更新中")
    article_title = db.Column(db.String(100), default="", comment="标题")
    article_price = db.Column(db.String(10), default="0", comment="节价格")
    is_pay = db.Column(db.String(5), default="1", comment="是否付费")
    is_trials = db.Column(db.String(5), default="0", comment="是否为试读")
    pic_url = db.Column(db.String(200), default="", comment="图片地址")
    chapter_id = db.Column(db.String(50), comment="章id")
    ebook_id = db.Column(db.String(50), comment="电子书id")




