
# encoding: utf-8

from flask import Flask
#from API.config import SECRET_KEY
#from passlib.apps import custom_app_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

class StudentNews(db.Model):
    __tablename__ = 'student_msg'
    #基础信息
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(5),nullable=True) #姓名
    sex = db.Column(db.String(3),nullable=True) #性别
    #非基础信息

    nstitute = db.Column(db.String(20),nullable=True) #学院
    major = db.Column(db.String(20),nullable=True) #专业
    grade = db.Column(db.String(20),nullable=True) #班级
    teacher = db.Column(db.String(5),nullable=True) #辅导员
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

class TeacherNews(db.Model):
    __tablename__ = 'teacher_msg'
    #辅导员
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Colimn(db.String(5),nullable=False)

