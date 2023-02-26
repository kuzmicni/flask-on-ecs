from flask import Flask, jsonify, request
import pickle
import numpy as np
import xgboost as xgb

def puppy_type(prediction):
    if int(prediction[0]) == 0:
        puppy = 'wiener dog'
    elif int(prediction[0]) == 1:
        puppy = 'german shepherd'
    else:
        puppy = 'something went wrong'
    return puppy

flask_app_obj = Flask(__name__)

with open('model.pkl', 'rb') as f:
    ml_model = pickle.load(f)

@flask_app_obj.route('/')
def hi_there():
    return 'Hola, Amigos!'

@flask_app_obj.route("/recms", methods = ["POST"])
def make_rec():
  if request.method == "POST":
        data = request.get_json() 
        area = int(data["area"])
        print(area)
        input_value = np.array([[area]])
        # Test API: curl -X POST http://0.0.0.0:80/recms -H 'Content-Type: application/json' -d '{"area":"200"}'
        try: 
            print(input_value)
            prediction = ml_model.predict(input_value)
            puppy_rec = puppy_type(prediction)
            
        except Exception as e:
            puppy_rec = None
            print("An error occurred:", e)
        
        return {"rec_puppy":puppy_rec}

if __name__ == "__main__":
    flask_app_obj.run(host='0.0.0.0', port=80)
