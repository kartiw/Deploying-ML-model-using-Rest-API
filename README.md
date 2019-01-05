# deploying_model_as_RESTful_webservice

## Files:
1. iris_classification_model.ipynb : A simple Logistic regression model for Iris dataset
2. app.py : Flask application to deploy the model and the RESTful API
3. calling_api.ipynb: Notebook to call the API.

## Execution order:

1. Run the app.py to start the webservice.
2. Use calling_api.ipynb to call the webservice. Chnage the 'features' list to predict the flower type. The featues list takes 4 values.

Note: If you wish to use a different model or retrain the model use the iris_classification_model.ipynb to do so.
