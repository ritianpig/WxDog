from WxDog.extensions import db, admin
from WxDog.models import Ebook, Chapter, Article
from flask_admin.contrib.sqla import ModelView


class BookView(ModelView):
    column_labels = dict(
        ebook_id=u'电子书id',
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
        chapter_id=u'章id',
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
        chapter_id=u'章id',
        ebook_id=u'电子书id'
    )


admin.add_view(BookView(Ebook, db.session, name="电子书"))
admin.add_view(ChapterView(Chapter, db.session, name="章"))
admin.add_view(ArticleView(Article, db.session, name="节"))
