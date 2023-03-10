# import json
# from py_edamam import Edamam

class Nutrients:

    def __init__(self):
        self.name = ""

        self.calories = 0
        self.calorieDaily = ""

        self.fat = ""
        self.fatDaily = ""
        self.saturatedFat = ""
        self.saturatedFatDaily = ""

        self.cholesterol = ""
        self.cholesterolDaily = ""
        self.sodium = ""
        self.sodiumDaily = ""

        self.carbohydrates = ""
        self.carbohydratesDaily = ""
        self.fiber = ""
        self.fiberDaily = ""
        self.sugar = ""

        self.protein = ""
        self.proteinDaily = ""

        self.calcium = ""
        self.calciumDaily = ""
        self.magnesium = ""
        self.magnesiumDaily = ""
        self.potassium = ""
        self.potassiumDaily = ""
        self.iron = ""
        self.ironDaily = ""
        self.zinc = ""
        self.zincDaily = ""
        self.phosphorus = ""
        self.phosphorusDaily = ""

        self.vitaminA = ""
        self.vitaminADaily = ""
        self.vitaminC = ""
        self.vitaminCDaily = ""
        self.vitaminB6 = ""
        self.vitaminB6Daily = ""
        self.vitaminB12 = ""
        self.vitaminB12Daily = ""
        self.vitaminD = ""
        self.vitaminDDaily = ""

    def getCalories(self, total, daily):
        self.calories = str(round(float(total["ENERC_KCAL"]["quantity"])))
        self.calorieDaily = str(round(float(daily["ENERC_KCAL"]["quantity"]), 1)) + daily["ENERC_KCAL"]["unit"]

    def getFats(self, total, daily):
        self.fat = str(round(float(total["FAT"]["quantity"]), 1)) + total["FAT"]["unit"]
        self.fatDaily = str(round(float(daily["FAT"]["quantity"]), 1)) + daily["FAT"]["unit"]
        try:
            self.saturatedFat = str(round(float(total["FASAT"]["quantity"]), 1)) + total["FASAT"]["unit"]
            self.saturatedFatDaily = str(round(float(daily["FASAT"]["quantity"]), 1)) + daily["FASAT"]["unit"]
        except KeyError:
            self.saturatedFat = "0g"
            self.saturatedFatDaily = "0%"

    def getCholesterol(self, total, daily):
        try:
            self.cholesterol = str(round(float(total["CHOLE"]["quantity"]), 1)) + total["CHOLE"]["unit"]
            self.cholesterolDaily = str(round(float(daily["CHOLE"]["quantity"]), 1)) + daily["CHOLE"]["unit"]
        except KeyError:
            self.cholesterol = "0mg"
            self.cholesterolDaily = "0%"
        self.sodium = str(round(float(total["NA"]["quantity"]), 1)) + total["NA"]["unit"]
        self.sodiumDaily = str(round(float(daily["NA"]["quantity"]), 1)) + daily["NA"]["unit"]

    def getCarbs(self, total, daily):
        self.carbohydrates = str(round(float(total["CHOCDF"]["quantity"]), 1)) + total["CHOCDF"]["unit"]
        self.carbohydratesDaily = str(round(float(daily["CHOCDF"]["quantity"]), 1)) + daily["CHOCDF"]["unit"]
        self.fiber = str(round(float(total["FIBTG"]["quantity"]), 1)) + total["FIBTG"]["unit"]
        self.fiberDaily = str(round(float(daily["FIBTG"]["quantity"]), 1)) + daily["FIBTG"]["unit"]
        self.sugar = str(round(float(total["SUGAR"]["quantity"]), 1)) + total["SUGAR"]["unit"]

    def getProtein(self, total, daily):
        self.protein = str(round(float(total["PROCNT"]["quantity"]), 1)) + total["PROCNT"]["unit"]
        self.proteinDaily = str(round(float(daily["PROCNT"]["quantity"]), 1)) + daily["PROCNT"]["unit"]

    def getElements(self, total, daily):
        self.calcium = str(round(float(total["CA"]["quantity"]), 1)) + total["CA"]["unit"]
        self.calciumDaily = str(round(float(daily["CA"]["quantity"]), 1)) + daily["CA"]["unit"]
        self.magnesium = str(round(float(total["MG"]["quantity"]), 1)) + total["MG"]["unit"]
        self.magnesiumDaily = str(round(float(daily["MG"]["quantity"]), 1)) + daily["MG"]["unit"]
        self.potassium = str(round(float(total["K"]["quantity"]), 1)) + total["K"]["unit"]
        self.potassiumDaily = str(round(float(daily["K"]["quantity"]), 1)) + daily["K"]["unit"]
        self.iron = str(round(float(total["FE"]["quantity"]), 1)) + total["FE"]["unit"]
        self.ironDaily = str(round(float(daily["FE"]["quantity"]), 1)) + daily["FE"]["unit"]
        self.zinc = str(round(float(total["ZN"]["quantity"]), 1)) + total["ZN"]["unit"]
        self.zincDaily = str(round(float(daily["ZN"]["quantity"]), 1)) + daily["ZN"]["unit"]
        self.phosphorus = str(round(float(total["P"]["quantity"]), 1)) + total["P"]["unit"]
        self.phosphorusDaily = str(round(float(daily["P"]["quantity"]), 1)) + daily["P"]["unit"]

    def getVitamins(self, total, daily):
        self.vitaminA = str(round(float(total["VITA_RAE"]["quantity"]), 1)) + total["VITA_RAE"]["unit"]
        self.vitaminADaily = str(round(float(daily["VITA_RAE"]["quantity"]), 1)) + daily["VITA_RAE"]["unit"]
        try:
            self.vitaminC = str(round(float(total["VITC"]["quantity"]), 1)) + total["VITC"]["unit"]
            self.vitaminCDaily = str(round(float(daily["VITC"]["quantity"]), 1)) + daily["VITC"]["unit"]
        except KeyError:
            self.vitaminC = "mg"
            self.vitaminCDaily = "0%"
        self.vitaminB6 = str(round(float(total["VITB6A"]["quantity"]), 1)) + total["VITB6A"]["unit"]
        self.vitaminB6Daily = str(round(float(daily["VITB6A"]["quantity"]), 1)) + daily["VITB6A"]["unit"]
        try:
            self.vitaminB12 = str(round(float(total["VITB12"]["quantity"]), 1)) + total["VITB12"]["unit"]
            self.vitaminB12Daily = str(round(float(daily["VITB12"]["quantity"]), 1)) + daily["VITB12"]["unit"]
        except KeyError:
            self.vitaminB12 = "0mg"
            self.vitaminB12Daily = "0%"

    def getAll(self, total, daily):
        self.getCalories(total, daily)
        self.getFats(total, daily)
        self.getCholesterol(total, daily)
        self.getCarbs(total, daily)
        self.getProtein(total, daily)
        self.getElements(total, daily)
        self.getVitamins(total, daily)

        return (f"Predicted food: {self.name} \n"
                f"Calories: {str(self.calories)}\t\t\t\t{self.calorieDaily}\n"
                f"Total fat: {self.fat}\t\t\t\t{self.fatDaily}\n\tSaturated fat: {self.saturatedFat}\t\t\t{self.saturatedFatDaily}\n"
                f"Cholesterol: {self.cholesterol}\t\t\t\t{self.cholesterolDaily}\nSodium: {self.sodium}\t\t\t\t{self.sodiumDaily}\n"
                f"Carbohydrates: {self.carbohydrates}\t\t\t\t{self.carbohydratesDaily}\n\tFiber: {self.fiber}\t\t\t{self.fiberDaily}\n\tSugar: {self.sugar}\n"
                f"Protein: {self.protein}\t\t\t\t{self.proteinDaily}\n"
                f"Calcium: {self.calcium}\t\t\t\t{self.calciumDaily}\n"
                f"Magnesium: {self.magnesium}\t\t\t\t{self.magnesiumDaily}\n"
                f"Potassium: {self.potassium}\t\t\t\t{self.potassiumDaily}\n"
                f"Iron: {self.iron}\t\t\t\t{self.ironDaily}\n"
                f"Zinc: {self.zinc}\t\t\t\t{self.zincDaily}\n"
                f"Vitamin A: {self.vitaminA}\t\t\t\t{self.vitaminA}\n"
                f"Vitamin C: {self.vitaminC}\t\t\t\t{self.vitaminCDaily}")

# e = Edamam(nutrition_appid='60411624', nutrition_appkey='d51c2c10fb84b7f5cb6c470dda575338')
# food = input()
# try:
#     fruit = e.search_nutrient("1 " + food)
#     x = json.dumps(fruit)  # deserializing dict
#     y = json.loads(x)
#     fruitItem = Nutrients()
#     fruitItem.name = food
#     fruitItem.getAll(y["totalNutrients"], y["totalDaily"])
# except:
#     print("No fruit found")
