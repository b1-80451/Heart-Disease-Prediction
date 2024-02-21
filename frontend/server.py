from flask import Flask, request, render_template
import pickle

# load the model
with open('/home/aditi/Sunpy/ML-JUPYTER/Project/model/Catboost.pkl', 'rb') as file:
    model = pickle.load(file)
    
with open('/home/aditi/Sunpy/ML-JUPYTER/Project/model/LabelEncode.pkl', 'rb') as file:
    encoder = pickle.load(file)


# create a flask application
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    # read the file contents and send them to client
    return render_template('form.html')


@app.route("/classify", methods=["POST"])
def classify():
    # get the values entered by user
    print(request.form)

    age = float(request.form.get("age"))
    gender = (request.form.get("gender"))
    ChestPainType = (request.form.get("chest-pain-type"))
    RestingBP = float(request.form.get("resting-bp"))
    totChol = float(request.form.get("cholesterol"))
    FastingBS = float(request.form.get("fasting-bs"))
    ECG= (request.form.get("resting-ecg"))
    MaxHR = float(request.form.get("max-hr"))
    ExerciseAngina = (request.form.get("exercise-angina"))
    Oldpeak = float(request.form.get("oldpeak"))
    ST_Slope = (request.form.get("st-slope"))



    answers = model.predict([
        [age,gender, ChestPainType, RestingBP, totChol, FastingBS, ECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]
    ])

    if answers[0] == 1:
        result = f"God may bless you!!! You will be suffering with Heart Disease"
    else:
        result = "Congrats!!! you wont be suffering with Heart Disease"

    return render_template(template_name_or_list='result.html',result=result)


# start the application
app.run(host="0.0.0.0", port=8000, debug=True)