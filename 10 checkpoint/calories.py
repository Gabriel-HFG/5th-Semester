def main():
    food = {
        "milk": 73,
        "almondmilk": 30,
        "yogurt": 75,
        "greekyogurt": 120,
        "egg": 75,
        "eggwhite": 17,
        "cheese": 79,
        "creamcheese": 51,
        "almonds": 170,
        "cashews": 163,
        "beans": 127,
        "blackbeans": 114,
        "broccoli": 55,
        "cauliflower": 25,
        "apple": 95,
        "banana": 105,
        "watermelon": 86,
        "orange": 73,
        "oatmeal": 77,
    }

    food_things = input("Enter food: ").lower()
    food_things_2 = input("Enter another food: ").lower()
    calculate(food_things, food_things_2, food)

def calculate(item1, item2, food):
    if item1 in food and item2 in food:
        if item1 == "watermelon" and item2 == "milk" or item1 == "milk" and item2 == "watermelon":
            print("Interesting combo! Watermelon and milk are not usually eaten together.")

        print(f"{item1} has {food[item1]} calories.")
        print(f"{item2} has {food[item2]} calories.")
        print(f"Together, they have {food[item1] + food[item2]} calories.")
    else:
        print(f"Sorry, I don't have information on {food}.")

main()