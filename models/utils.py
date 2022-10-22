import json
import pickle
import numpy as np
import pandas as pd
import config

class MedicalInsurance():

    def __init__(self, age, sex, bmi, children, smoker, region):

        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region

    def load_model(self):

        with open (config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open (config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model()

        region_index = self.json_data["columns"].index(self.region)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.age
        array[1] = self.json_data["sex_values"][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data["smoker_value"][self.smoker]
        array[region_index] = 1

        print("Test array ==>>\n", array)
        predicted_price = self.model.predict([array])[0]

        return np.around(predicted_price, 2)

if __name__ == "__main__":

    age = 60
    sex = "male"
    bmi = 22
    children = 1
    smoker = "no"
    region = "southeast"


    obj = MedicalInsurance(age, sex, bmi, children, smoker, region)
    price = obj.get_predicted_price()
    print(f"Your Predicted Price for Medical Insurance is {price}")

