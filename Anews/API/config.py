# encoding :utf-8
import os


DEBUG = True
SECRET_KEY = "S83rQ53gC4vdarcIAvY89Ky4"
HOST = '127.0.0.1'
PORT = '5000'
DATABASE = 'shcoolNews' # 数据库
USERNAME = 'qiaoshangwuxin'
PASSWORD = 'qiaoxiawuqing'
DB_URL = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True