# Import libraries
import joblib
import numpy as np

# Create inference functions
def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/best_model.joblib")
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == 'text/csv':
        data = np.fromstring(request_body, dtype=float, sep=',')
        return data
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")
