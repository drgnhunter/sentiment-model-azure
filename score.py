import os
import pickle
import json

# Called when the service is- initialized
def init():
    global model
    # The 'AZUREML_MODEL_DIR' environment variable indicates
    # where the model file is located in the deployment.
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "sentiment_model.pkl")
    
    # Load the model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

# Called for every- API request
def run(raw_data):
    try:
        # Load the JSON data. We expect a list of strings.
        data = json.loads(raw_data)
        
        # Make predictions
        predictions = model.predict(data)
        
        # Return the predictions as a JSON list
        return json.dumps(predictions.tolist())
        
    except Exception as e:
        return json.dumps({"error": str(e)})