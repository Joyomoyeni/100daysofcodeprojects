MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def coin():
    print("Please insert coins.")
    quarter = int(input("How many quarters?:"))
    dime = int(input("How many dimes?:"))
    nickle = int(input("How many nickels?:"))
    penny = int(input("How many pennies?:"))
    total = (0.25 * quarter) + (0.01 * penny) + (0.1 * dime) +(0.05 * nickle)
    return total
on_off = "on"

while on_off == "on":
    prompt = input("What would you like? (expresso/latte/cappuccino): ")
    if(prompt == "latte"):
        if(resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"] and resources["water"] >= MENU["latte"]["ingredients"]["water"]):
            change = round(coin() - MENU["latte"]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
            profit = profit + MENU["latte"]["cost"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"]  = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            print("Here is your latte. Enjoy!!!")
        else:
            on_off = "off"
    elif(prompt == "espresso"):
        if(resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"] and resources["water"] >= MENU["espresso"]["ingredients"]["water"]):
            change = round(coin() - MENU["espresso"]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
            resources["coffee"]  = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            profit = profit + MENU["espresso"]["cost"]
            print("Here is your espresso. Enjoy!!!")
        else:
            on_off = "off"
    elif(prompt == "cappuccino"):
        if(resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"] and resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]):
            change = round(coin() - MENU["cappuccino"]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            profit = profit + MENU["cappuccino"]["cost"]
            print("Here is your cappuccino. Enjoy!!!")
        else:
            on_off = "off"
    elif(prompt == "report"):
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    elif(prompt == "off"):
        on_off = "off"
if (on_off == "off"):
    print("Byee!!")
