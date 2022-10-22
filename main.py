import config
from flask import Flask, jsonify, render_template, request
from models.utils import MedicalInsurance

app = Flask(__name__)

@app.route("/")

def hello_flask():
    print("Welcome to Medical Insurance Price Predictor")
    # return "Success"
    return render_template("index.html")

@app.route("/predicted_price", methods = ["POST", "GET"])

def get_insu_price():

    if request.method == "GET":
        print("We are using GET method")

        # input_data = request.form
        # print("DATA ==>>", input_data)

        # age = eval(input_data['age'])
        # sex = input_data['sex']
        # bmi = eval(input_data['bmi'])
        # children = eval(input_data['children'])
        # smoker = input_data['smoker']
        # region = input_data['region']


        age = int(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = int(request.args.get('bmi'))
        children = int(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')


        print("age, sex, bmi, children, smoker, region\n", age, sex, bmi, children, smoker, region)



        obj = MedicalInsurance(age, sex, bmi, children, smoker, region)
        price = obj.get_predicted_price()
        # return jsonify ({"Result" : (f"Your Predicted Price for Medical Insurance is {price}")})
        return render_template("index.html", prediction = price)



    else:
        print("We are using POST method")

        age = int(request.form.get('age'))
        sex = request.form.get('sex')
        bmi = int(request.form.get('bmi'))
        children = int(request.form.get('children'))
        smoker = request.form.get('smoker')
        region = request.form.get('region')
        

        print("age, sex, bmi, children, smoker, region\n", age, sex, bmi, children, smoker, region)



        obj = MedicalInsurance(age, sex, bmi, children, smoker, region)
        price = obj.get_predicted_price()
        # return jsonify ({"Result" : (f"Your Predicted Price for Medical Insurance is {price}")})
        return render_template("index.html", prediction = price)






if __name__ == "__main__":

    app.run(host="0.0.0.0", port=config.PORT_NUMBER, debug=True)