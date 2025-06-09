from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('model_churn_pred.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        # Handle JSON POST
        data = request.get_json(force=True)
        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)
        return jsonify({'churn_prediction': int(prediction[0])})
    else:
        # Handle form POST
        data = request.form.to_dict()
        # Convert numeric fields
        for key in data:
            try:
                data[key] = float(data[key]) if '.' in data[key] else int(data[key])
            except ValueError:
                pass
        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)
        if int(prediction[0]) == 1:
            prediction_text = 'Customer will more likely to left the company'
            prediction_class = 'prediction-red'
        else:
            prediction_text = 'It is Loyal customer'
            prediction_class = 'prediction-green'
        return render_template('index.html', prediction_text=prediction_text, prediction_class=prediction_class)

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True) 