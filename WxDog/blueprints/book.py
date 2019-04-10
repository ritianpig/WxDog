from flask import Blueprint


book = Blueprint("book", __name__)
@book.route('/bok', methods=["GET", "POST"])
def bok():
    return "ok"