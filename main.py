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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calc_resources(user_choice,resources):
    if money_calc(quaters,dimes,nickles,pennies):
        for i in MENU[user_choice]['ingredients']:
         resources[i] -= MENU[user_choice]['ingredients'][i]
        # new_resources['water'] =
        # resources['water'] -= MENU[user_choice]['ingredients']['water']

    return resources

    # else:
    #     return


def money_calc(quaters,dimes,nickles,pennies):
    quaters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01
    total = quaters+ dimes+ nickles+ pennies
    if total >= MENU[user_choice]['cost']:
        total -= MENU[user_choice]['cost']
        print(f"Here is your {user_choice}")
        # new_resources = calc_resources(user_choice,resources)
        remaining_change= round(total,2)
        print(f"Here is {remaining_change} in change")
        return True
    else:
        print("Insfficient fund")
        return False


to_continue = True
new_resources = resources

while to_continue :
    user_choice = input("What would you like to have - ESPRESSO or LATTE or CAPPUCCINO\n").lower()

    # print(resources)
    if MENU[user_choice]['ingredients']['water'] <= new_resources['water']:
        quaters = int(input("Insert Coins\nhow many quaters"))
        dimes = int(input("how many dimes "))
        nickles = int(input("how many nickles "))
        pennies = int(input("how many pennies "))
        # money_calc(quaters, dimes, nickles, pennies)
        new_resources = calc_resources(user_choice,resources)
        print(new_resources)

    else:
        to_continue = False
        print("we're ran out of ingredients")