import json

from datetime import datetime
from flask import Blueprint, request, jsonify
from WxDog.models import Ebook, UserBuys, Article, Chapter
from WxDog.extensions import db


book = Blueprint("book", __name__)


@book.route('/getdata', methods=["GET", "POST"])
def getdata():
    get_page = request.args.get("num")
    books = Ebook.query.all()
    paginates = Ebook.query.paginate(int(get_page), per_page=10).items
    data_list = []
    for book in paginates:
        data = {
            "ebook_id": book.ebook_id,
            "classification": book.classification,
            "ebook_title": book.ebook_title,
            "introduce": book.introduce,
            "envelope_url": book.envelope_url,
            "ebook_price": book.ebook_price,
            "total_chapter": book.total_chapter,
            "is_pay": book.is_pay,
            "free_trials": book.free_trials
        }
        data_list.append(data)
    result = {
        "num": len(books),
        "data": data_list
    }
    return jsonify(result)


@book.route('/update', methods=["GET", "POST"])
def update():
    if request.method == "POST":
        get_data = request.get_data()
        data_dic = json.loads(get_data)
        if data_dic["ebook_id"]:
            ebook_id = data_dic["ebook_id"]
            res_book = Ebook.query.filter_by(ebook_id=ebook_id).first()
            if res_book:
                res_book.classification = data_dic["classification"]
                res_book.ebook_title = data_dic["ebook_title"]
                res_book.introduce = data_dic["introduce"]
                res_book.envelope_url = data_dic["envelope_url"]
                res_book.ebook_price = data_dic["ebook_price"]
                res_book.total_chapter = data_dic["total_chapter"]
                res_book.is_pay = data_dic["is_pay"]
                res_book.free_trials = data_dic["free_trials"]
                db.session.commit()
                return jsonify({"message": "修改成功"})
            else:
                return jsonify({"message": "ebook_id不存在"})
        else:
            return jsonify({"message": "ebook_id必填"})


@book.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        get_data = request.get_data()
        data_dic = json.loads(get_data)
        ebook_id = data_dic["ebook_id"]
        if ebook_id:
            res_ebook = Ebook.query.filter_by(ebook_id=ebook_id).first()
            db.session.delete(res_ebook)
            db.session.commit()
        return jsonify({"message": "ok"})


@book.route('/adddata', methods=["GET", "POST"])
def adddata():
    if request.method == "POST":
        get_data = request.get_data()
        data_dic = json.loads(get_data)
        ebook_id = data_dic["ebook_id"]
        classification = data_dic["classification"]
        ebook_title = data_dic["ebook_title"]
        introduce = data_dic["introduce"]
        envelope_url = data_dic["envelope_url"]
        ebook_price = data_dic["ebook_price"]
        total_chapter = data_dic["total_chapter"]
        is_pay = data_dic["is_pay"]
        free_trials = data_dic["free_trials"]
        res_book = Ebook.query.filter_by(ebook_id=ebook_id).first()
        if res_book:
            return jsonify({"message": "ebook_id已存在"})
        else:
            add_book = Ebook(ebook_id=ebook_id, classification=classification,
                             ebook_title=ebook_title, introduce=introduce,
                             envelope_url=envelope_url, ebook_price=ebook_price,
                             total_chapter=total_chapter, is_pay=is_pay,
                             free_trials=free_trials)
            db.session.add(add_book)
            db.session.commit()
            return jsonify({"message": "添加成功"})



@book.route('/ebook', methods=["GET", "POST"])
def ebook():
    if request.method == "GET":
        return "仅支持POST请求"
    else:
        get_data = request.get_data()

        show_class = request.headers.get("ShowClass")
        class_name = request.headers.get("ClassName")
        get_book = request.headers.get("GetBook")
        get_article = request.headers.get("GetArticle")


        if show_class:
            res_ebooks = Ebook.query.all()
            class_list = []
            if res_ebooks:
                for ebook in res_ebooks:
                    class_list.append(ebook.classification)
                class_list = list(set(class_list))
            else:
                pass
            return jsonify({"class_list": class_list})

        if class_name:
            data_dic = json.loads(get_data)
            class_name = data_dic["class_name"]
            openid = data_dic["openid"]
            page = data_dic["page"]
            res_ebooks = Ebook.query.filter_by(classification=class_name).all()
            if res_ebooks:
                book_list = []
                index1 = page * 6
                index2 = (page + 1) * 6
                part_list = res_ebooks[index1:index2]
                for book in part_list:

                    try:
                        last_time = Article.query.filter_by(
                            ebook_id=book.ebook_id).order_by(
                            Article.enter_date.desc()).first().enter_date
                    except:
                        last_time = datetime.now()

                    res_user_buys = UserBuys.query.\
                        filter_by(openid=openid, ebook_id=book.ebook_id).first()
                    is_buy = "1" if res_user_buys else "0"

                    book_dic = {
                        "class_name": class_name,
                        "ebook_id": book.ebook_id,
                        "ebook_title": book.ebook_title,
                        "envelope_url": book.envelope_url,
                        "is_buy": is_buy,
                        "enter_data": str(last_time)
                    }
                    book_list.append(book_dic)
                return jsonify({"ebook_list": book_list})
            else:
                return "No {} ebook".format(class_name)

        if get_book:
            data_dic = json.loads(get_data)
            ebook_id = data_dic["ebook_id"]
            openid = data_dic["openid"]

            res_ebook = Ebook.query.filter_by(ebook_id=ebook_id).first()
            res_user_buys = UserBuys.query. \
                filter_by(openid=openid, ebook_id=ebook_id).first()
            is_buy = "1" if res_user_buys else "0"

            if res_ebook:
                res_chapters = Chapter.query.filter_by(ebook_id=ebook_id).all()
                try:
                    last_time = Article.query.filter_by(ebook_id=ebook_id).\
                        order_by(Article.enter_date.desc()).first().enter_date
                except:
                    last_time = datetime.now()
                if res_chapters:
                    result_list = []
                    for chapter in res_chapters:
                        res_articles = Article.query.filter_by(
                            ebook_id=ebook_id,
                            chapter_id=chapter.chapter_id).all()

                        article_list = []
                        if res_articles:
                            for article in res_articles:
                                article_dic = {
                                    "article_title": article.article_title,
                                    "article_id": article.article_id
                                }
                                article_list.append(article_dic)
                        else:
                            pass
                        chapter_dic = {
                            "chapter_title": chapter.chapter_title,
                            "article_list": article_list
                        }
                        ebook_introduce = res_ebook.introduce
                        envelope_url = res_ebook.envelope_url
                        result_dic = {
                            "ebook_introduce": ebook_introduce,
                            "chapter": chapter_dic,
                            "enter_date": str(last_time),
                            "envelope_url": envelope_url,
                            "is_buy": is_buy
                        }
                        result_list.append(result_dic)
                    return jsonify(result_list)
                else:
                    return jsonify({})

        if get_article:
            data_dic = json.loads(get_data)
            article_id = data_dic["article_id"]
            res_article = Article.query.filter_by(article_id=article_id).first()
            if res_article:
                article_dic = {
                    "article_id": article_id,
                    "article_title": res_article.article_title,
                    "content": res_article.content,
                    "pic_url": res_article.pic_url
                }

                return jsonify(article_dic)
            else:
                return "没有内容"


