from flask import Flask, jsonify, request
import pickle
import numpy as np
import xgboost as xgb

flask_app_obj = Flask(__name__)

with open('model.pkl', 'rb') as f:
    ml_model = pickle.load(f)

@flask_app_obj.route('/')
def hi_there():
    return 'Hi, there!'

@flask_app_obj.route("/recms", methods = ["POST"])
def make_rec():
  if request.method == "POST":
        data = request.get_json() 
        yrs = float(data["years"])
        input_value = np.array([[yrs]])
        # Test API: curl -X POST http://0.0.0.0:80/recms -H 'Content-Type: application/json' -d '{"years":"2.5"}'
        try: 
            prediction = ml_model.predict(input_value)[0]
            
            
        except Exception as e:
            prediction = None
            print("An error occurred:", e)
        
        return {"salary":str(prediction)}

if __name__ == "__main__":
    flask_app_obj.run(host='0.0.0.0', port=80)
