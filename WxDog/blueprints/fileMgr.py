import json
import os

from flask import Blueprint, request, jsonify, render_template



fileMgr = Blueprint("fileMgr", __name__)

@fileMgr.route("/uploads", methods=['POST', 'GET'])
def uploads():
    UPLOAD_PATH = "/home/lmc/workspace/WorkProjects/WxDog/WxDog/static/pic/"
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(UPLOAD_PATH, f.filename))
        print(os.path.getsize(UPLOAD_PATH + f.filename))
    return render_template('uploads.html')

@fileMgr.route("/showPic", methods=['POST', 'GET'])
def showPic():
    srcDir = "/home/lmc/workspace/WorkProjects/WxDog/WxDog/static/pic/"
    fileList = os.listdir(srcDir)
    sendFileList = []
    for fileName in fileList:
        sendFileList.append(fileName)
    if request.method == "GET":
        return render_template("showPic.html", pics = sendFileList)

@fileMgr.route("/searchPic", methods=['GET', 'POST'])
def search():
    srcDir = "/home/lmc/workspace/WorkProjects/WxDog/WxDog/static/pic/"
    fileList = os.listdir(srcDir)
    sendFileList = []
    message = "0"
    if request.method == 'POST':
        get_data = request.get_data()
        data_dic = json.loads(get_data)
        key = data_dic["picName"]
        for fileName in fileList:
            if key in str(fileName):
                message = "1"
                sendFileList.append(fileName)
        return jsonify({"resPicNameList": sendFileList, "message": message})

@fileMgr.route("/allFile", methods=["GET", "POST"])
def allFile():
    srcDir = "/home/lmc/workspace/WorkProjects/WxDog/WxDog/static/pic/"
    fileList = os.listdir(srcDir)
    sendFileList = []
    for fileName in fileList:
        sendFileList.append(fileName)
    if request.method == "GET":
        return render_template("fileMgr.html", pics=sendFileList)


@fileMgr.route("/delPic", methods=["GET", "POST"])
def delPic():
    srcDir = "/home/lmc/workspace/WorkProjects/WxDog/WxDog/static/pic/"
    if request.method == "POST":
        get_data = request.get_data()
        data_list = json.loads(get_data)
        try:
            for fileName in data_list:
                wholeFileName = srcDir + fileName
                os.remove(wholeFileName)
            resJson = {"message": "1"}
        except:
            resJson = {"message": "2"}
        return jsonify(resJson)

