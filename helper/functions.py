import json

def load_food_data():
    with open("helper/data.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def get_food_information(food):
    """
    Get food information
    """
    food_information = load_food_data()
    food = food.lower() 

    if food in food_information:
        return food_information[food]
    else:
        return "Food information not found"
    
    