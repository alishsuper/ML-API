import sys
import os
import logging
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/api/winequality/query',methods=['POST','GET'])
def query_classiffier():
    try:
        req_json = request.get_json()
	if req_json is None:
	    return jsonify( error = 'this service require A JSON request' )

        fixed_acidity = float(req_json['fixed acidity'])
        volatile_acidity = float(req_json['volatile acidity'])
        citric_acid = float(req_json['citric acid'])
        residual_sugar = float(req_json['residual sugar'])
        chlorides = float(req_json['chlorides'])
        free_sulfur_dioxide = float(req_json['free sulfur dioxide'])
        total_sulfur_dioxide = float(req_json['total sulfur dioxide'])
        density = float(req_json['density'])
        pH = float(req_json['pH'])
        sulphates = float(req_json['sulphates'])
        alcohol = float(req_json['alcohol'])

	wine_train = pd.read_csv('/var/python-app/winequality-red.csv', sep=";")
	X = wine_train.drop(['quality'], axis='columns').values
	y = wine_train['quality'].values
	ss = StandardScaler()
	X_train = ss.fit_transform(X)
	rf = RandomForestClassifier(n_estimators=100, max_depth=11, random_state=100)
	rf = rf.fit(X_train, y)

	X_val = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol])

	quality = float(rf.predict(X_val))
        return jsonify(quality=quality)

    except Exception as ex:
       app.log.error(type(ex))
       app.log.error(ex.args)
       app.log.error(ex)
       return jsonify(error = str(ex))

if __name__ == '__main__':

    LOG_FORMAT = "'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
    logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT)
    app.log = logging.getLogger(__name__)

    port = os.environ['FLASK_PORT']
    app.run(host='0.0.0.0',port=int(port),debug=False)
