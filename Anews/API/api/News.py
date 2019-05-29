# -*- coding: utf-8 -*-
from flask import Flask,redirect,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import SECRET_KEY
from Anews.etc import success_msg,fail_msg
from flask_restful import Resource,request
app = Flask(__name__)
CORS(app, supports_credentials=True) #跨域
@app.before_request   #钩子
def app_before_request():
  print("HTTP {}  {}".format(request.method, request.url))
@app.after_request
def app_after_request(response):
    response.header['Form'] = 'NCUHOME'
    return response


@app.route("/student/baseMessage/",methods=['POST'])
def studentNews():
    return
@app.route("/student/getPhone",methods=['GET'])
def Getphone():
    return

@app.route("/student/personalMessage",methods=['GET'])
def GetPersonalMessage():
    dict = request.get_json(force=True) #获取所有
    name =dict.get('name')

    Name = studentNews.query.filter_by(name=name).first()







if __name__ == '__main__':
    app.run(port=5000,host=0)
