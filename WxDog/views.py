from WxDog.extensions import db, admin
from WxDog.models import Ebook, Chapter, Article, User, UserBuys, VipOrder, Vip
from flask_admin.contrib.sqla import ModelView


class BookView(ModelView):
    column_list = ('ebook_id', 'classification', 'ebook_title', 'introduce',
                   'envelope_url', 'ebook_price', 'total_chapter', 'is_pay',
                   'free_trials')
    column_labels = dict(
        ebook_id=u'电子书序号',
        classification=u'分类所属',
        ebook_title=u'电子书标题',
        introduce=u'简介',
        envelope_url=u'封皮地址',
        ebook_price=u'电子书价格',
        total_chapter=u'总章数',
        is_pay=u'是否付费',
        free_trials=u'免费试读章数'
    )


class ChapterView(ModelView):
    column_labels = dict(
        ebook=u'电子书',
        chapter_id=u'章序号',
        chapter_title=u'章标题',
        chapter_price=u'章价格',
        is_pay=u'是否付费',
        is_trials=u'是否为试读',
        ebook_id=u'电子书id'
    )


class ArticleView(ModelView):
    column_labels = dict(
        is_update=u'是否更新中',
        article_title=u'节标题',
        article_price=u'节价格',
        is_pay=u'是否付费',
        is_trials=u'是否为试读',
        pic_url=u'图片地址',
        chapter_id=u'章序号',
        ebook_id=u'电子书序号',
        content=u'内容',
        enter_date=u'创建日期'
    )

class UserView(ModelView):
    column_labels = dict(
        other_name=u'昵称',
        sex=u'性别',
        age=u'年龄',
        area=u'区域',
        income=u'收入',
        want_buy=u'购买意向',
        telnum=u'电话号码',
        typephone=u'手机型号',
        grade_vip=u'会员等级',
        add_date=u'入库时间'
    )


class VipView(ModelView):
    column_labels = dict(
        id=u'序号',
        name=u'会员名',
        grade=u'会员等级',
        introduce=u'权益介绍',
        price=u'价格'
    )


class Buy_view(ModelView):
    column_labels = dict(
        ebook_id=u'电子书id',
        buydate=u'购买日期'
    )

class VipRecordView(ModelView):
    column_labels = dict(
        grade=u'vip等级',
        buy_date=u'购买日期',
        lose_date=u'失效日期'
    )


admin.add_view(BookView(Ebook, db.session, name="电子书"))
admin.add_view(ChapterView(Chapter, db.session, name="章"))
admin.add_view(ArticleView(Article, db.session, name="节"))
admin.add_view(UserView(User, db.session, name="用户表"))
admin.add_view(Buy_view(UserBuys, db.session, name="电子书订单表"))
admin.add_view(VipView(Vip, db.session, name="Vip表"))
admin.add_view(VipRecordView(VipOrder, db.session, name="Vip订单表"))
