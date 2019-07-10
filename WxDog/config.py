import os

# MySQL connection
dev_db = 'mysql+pymysql://root:123456@127.0.0.1:3306/wxdog?charset=utf8'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
Debug = False
JSON_AS_ASCII = False
DROPZONE_REDIRECT_VIEW = "fileMgr.showPic"
DROPZONE_MAX_FILE_SIZE = 4096
DROPZONE_FILE_TOO_BIG = "上传文件过大"
DROPZONE_SERVER_ERROR = "服务器错误"
DROPZONE_TIMEOUT = 3000000
# MAX_CONTENT_LENGTH = 2 * 1024 * 1024 * 1024