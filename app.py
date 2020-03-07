import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) 
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    probability = model.predict_proba(final_features)

    if prediction[0] == 1:
        output = 'Yes'
        probability = probability[0][1]
    else:
        output = 'No'
        probability = probability[0][0]
    prediction_text_result = 'Will the person default on the next month payment?\n- {} with {:2.2%} probability'.format(output, probability)
    if request.is_xhr:
       return jsonify({'prediction_text': prediction_text_result, 'result': output})
    return render_template('index.html', prediction_text = prediction_text_result)

if __name__ == "__main__":
    app.run()

