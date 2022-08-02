from flask import Flask, request, render_template, jsonify
import os
import pickle
import pandas as pd
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():        
    return render_template('server.html')    

@app.route('/', methods=['POST'])
def redirect_predict():    
    return predict()
    
@app.route('/predict')
def predict():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict_post():
    cluster_info = {}
    values = request.form
    if values:
        result = int(identify_cluster(values))
        if result:
            cluster_info['id'] = result

            # open and reading from churn_rate json file
            f = open ('./data/churn_rate_info.json', "r")
            data = json.loads(f.read())
            print(data[str(result)])    
            cluster_info['churn %'] = data[str(result)]
            # Closing file
            f.close()

             # open and reading from gender json file
            f = open ('./data/gender_info.json', "r")
            data = json.loads(f.read())
            print(data[str(result)])    
            cluster_info['female %'] = data[str(result)]
            # Closing file
            f.close()

            return render_template('result.html', result=cluster_info)
        else:
            return jsonify({
            "ERROR": "The cluster was not identified."
            })
    else:
        return jsonify({
            "ERROR": "No values were returned."
        })

def identify_cluster(values):
    # load the model from disk
    model = pickle.load(open('.\model\clustering_model.sav', 'rb'))
    # convert the dictionary into dataframe
    input_df = pd.DataFrame([values])
    # predict the cluster id
    cluster = model.predict(input_df)

    return cluster[0]

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)