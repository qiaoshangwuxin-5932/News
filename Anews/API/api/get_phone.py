# encoding: utf-8

from flask_restful import Resource,request
from flask import g
from API.models import StudentNews
from API.etc import success_msg,fail_msg,to_dict

class get_phone(Resource):
    '获取班级通讯录'
    @auth.login_required
    def get(self):
        data = request.get_json(force=True)
        id = data,get('id')
        nstitute = data.get('nstitute') #学院
        major = data.get('major')   #专业
        grade = data.get('grade')  #班级
        phone = StudentNews.query.filter_by(nstitute=nstitute,major=major,grade=grade).first()
        if not phone:
            return fail_msg(msg='404')
        output = { }
        output['article'] = to_dict(article.__dict__.copy())
        if phone.com:
            output['comments'] = {to_dict(comment.__dict__.copy()) for comment in article.comments}
        else:
            output['comments'] = {}
        return jsonify(output)
