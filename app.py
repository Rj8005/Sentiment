from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
# Load your trained model
model = joblib.load('C:\\Users\\rahul\\OneDrive\\Desktop\\New folder\\logistic_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from request
    data = request.get_json(force=True)
    text = data['text']

    # Preprocess and predict
    processed_text = preprocess(text)  # Implement this function as in your notebook
    text_vector = vectorizer.transform([processed_text])
    prediction = model.predict(text_vector)

    # Return result
    result = {'sentiment': 'Positive' if prediction[0] == 1 else 'Negative'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
