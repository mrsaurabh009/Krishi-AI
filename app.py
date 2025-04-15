from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('crop_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            prediction = model.predict(data)[0]

            return render_template('form.html', result=prediction)
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
