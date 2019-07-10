import json
from urllib import request as req

from flask import Blueprint, request, jsonify
from WxDog.extensions import db
from WxDog.func.WXBizDataCrypt import WXBizDataCrypt
from WxDog.models import User


consumer = Blueprint("consumer", __name__)


@consumer.route('/gettoken', methods=["GET", "POST"])
def gettoken():
    if request.method == "GET":
        results_dict = {}

        appId = request.args.get('appid')
        get_appsecret = request.args.get('secret')
        get_token = request.args.get('token')
        encryptedData = request.args.get(
            'encryptedData', type=str).replace('%2B', '+')
        iv = request.args.get('iv').replace('%2B', '+')

        resp = req.urlopen("https://api.weixin.qq.com/sns/jscode2session?"
                           "appid={}""&secret={}&js_code={}&grant_type="
                           "authorization_code".format(appId, get_appsecret,
                                                       get_token))
        resp1 = resp.read().decode()
        resp2 = json.loads(resp1)

        keys_list = []
        for k in resp2.keys():
            keys_list.append(k)

        # 判断是否存在unionid
        if 'unionid' in keys_list:
            unionid = resp2['unionid']
            openid = resp2['openid']
            nickName = resp2['nickName']
            gender = resp2['gender']
            city = resp2['city']
            province = resp2['province']

            res_users = User.session.query.filter_by(unionid=unionid).first()
            if res_users:
                res_users.openid = openid
                res_users.unionid = unionid
                res_users.other_name = nickName
                res_users.sex = gender
                res_users.area = city
                db.session.commit()
                results_dict.update(unionid=unionid, openid=openid)
            else:
                add_user = User(unionid=unionid, openid=openid,
                                other_name=nickName, sex=gender, area=city)
                db.session.add(add_user)
                db.session.commit()
                results_dict.update(unionid=unionid, openid=openid)
            return jsonify(results_dict)

        # 当openid存在unionid不存在时需要解密获取unionid
        if 'openid' in keys_list and 'unionid' not in keys_list:
            sessionKey = resp2['session_key']
            pc = WXBizDataCrypt(appId, sessionKey)
            resPc = pc.decrypt(encryptedData, iv)
            unionid = resPc['unionId']
            openid = resPc['openId']
            nickName = resp2['nickName']
            gender = resp2['gender']
            city = resp2['city']
            province = resp2['province']

            res_users = User.query.filter_by(unionid=unionid).first()
            if res_users:
                res_users.openid = openid
                res_users.unionid = unionid
                res_users.other_name = nickName
                res_users.sex = gender
                res_users.area = city
                db.session.commit()
                results_dict.update(unionid=unionid, openid=openid)
            else:
                add_user = User(unionid=unionid, openid=openid,
                                other_name=nickName, sex=gender, area=city)
                db.session.add(add_user)
                db.session.commit()
                results_dict.update(unionid=unionid, openid=openid)
            return jsonify(results_dict)
        else:
            return '或许参数输入有误，获取unionid失败'