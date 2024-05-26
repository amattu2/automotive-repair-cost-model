from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class CostPredictor(Resource):
    def post(self):
        if not request.json:
            return "Invalid request. Please POST with application/json Content-Type."

        try:
            return prediction.predict_cost(request.json)
        except Exception as e:
            return "Unknown error occurred. Please try again later."

api.add_resource(CostPredictor, '/predict')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
