
import pickle
import flask

app = flask.Flask(__name__)

#getting our trained model from a file we created earlier
model = pickle.load(open("iris_model.pkl","rb"))

@app.route('/predict', methods=['POST'])
def predict():
	try:
		#grabbing a set of flower features from the request's body
		feature_array = flask.request.get_json(force=True)['feature_array']

		prediction = model.predict([feature_array]).tolist()

		#preparing a response object and storing the model's predictions
		response = {}
		response['predictions'] = prediction

		#sending our response object back as json
		return flask.jsonify(response)
	except:
		esponse = {}
		response["Internal Server Error"]=500
		return flask.jsonify(response)

if __name__=="__main__":
	app.run(port=9000, debug=True)
