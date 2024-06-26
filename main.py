from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_data', methods = ['POST'])
def model_prediction():
    data = request.form 

    model = pickle.load(open(r'logistic_model.pkl','rb'))
    
    user_data = [[float(data['age']),
                  float(data['length_of_service']),
                  float(data['avg_training_score']),
                  float(data['awards_won'])
                  ]]

    result = model.predict(user_data)

    target = ['not promoted', 'promoted']

    prediction = target[result[0]]
    print(prediction)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
