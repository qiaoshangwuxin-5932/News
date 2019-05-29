from flask_restful import Api
from flask_cors import CORS
from API import app
from API.api.get_phone import get_phone

CORS(app)
api = Api(app)
api.add_resource(get_phone,'/api/get_phone')


if __name__ == '__main__':
    app.run(debug=True)