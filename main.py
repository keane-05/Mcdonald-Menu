alc = { "Chicken Burger": 3 ,
        "Fille Ole Fish": 5,
        "Chesseburger":4,
        "Double Chesseburger": 6,
        "Chicken McNugget":4 ,
        "Nasi Lemak Burger":5,
        "Butermilk Crispy Chicken Burger":6,
        "McSpicy":5,
        "Big Mac":5,
        "Hamburger":5
        }
set_meals = {"Chicken Burger":8,
             "Fille Ole Fishl":6,
             "Chesseburger":6,
             "Double Chesseburger":8,
             "Chicken McNugget":7,
             "Nasi Lemak Burger ":9,
             "Butermilk Crispy Chicken Burger":10,
             "McSpicy ": 8,
             "Big Mac ":9,
             "Hamburger":8
             }
dessert = {"McFlurry": 5,
           "Vanilla Ice Cream":2,
           "Chococone":2.5,
           "Hot Fudge":3.4
           }
drinks = {"Pepsi", "Pepsi Black", "100 Plus", "Coke Zero"}
print("Welcome to MacDonalds!")
decision = int(input("What would you like to eat: \n1) Set Meal \n2) Ala carte\n3) Dessert\n"))

while True:
    if decision == 1:
        for food in set_meals.keys():
            print(food + " Meal" + "--------- " + str(set_meals.get(food)))
        change = input("\nDo you want to change your menu? Y/N: ")
        if change == "Y":
            go_back = input("Did you accidentally click? Y/N: ")
            if go_back == "Y":
                decision = 1
            elif go_back == "N":
                decision = int(input("What Do You Want To Change To:\n2) Ala Carte\n3) Dessert\n"))
                while decision != 2 and decision != 3:
                    decision = int(input("Invalid, Please enter the correct number: "))
            else:
                go_back= input("INVALID, Please give the correct value: ")
        elif change == "N":
            purchasing = input("What would you like to buy: ")
            if purchasing in (set_meals.keys()):
                print("Your price will be: "+ str(set_meals.get(food)))
                choice  = input("Are you sure this is the meal you want?: ")
                if choice == "Y":
                    payment = input("How do you want to pay?")
                else:
                    what_you_want = input("What do you want to buy instead: ")



        else:
            INVALID = input("Invalid, Please try again: ")
            while INVALID != "Y" and INVALID != "N":
                INVALID = input("Invalid, Please try again: ")
            if INVALID == "Y":
                decision = (input("What Do You Want To Change To:\n2) Ala Carte\n3) Dessert\n"))
            elif INVALID == "N":
                break

    elif decision == 2:
        for food in set_meals:
            print(food + "------")
        change = input("\nIf you do not want this, please put in another number Y/N: ")
        if change == "Y":
            decision = int(input("What Do You Want To Change To:\n1) Set Meal\n3) Dessert\n"))
            while decision != "1" and decision != "3":
                decision = input("Invalid, Please enter the correct number: ")
        elif change == "N":
            break
        else:
            INVALID = input("Invalid, Please try again: ")
            while INVALID != "Y" and INVALID != "N":
                INVALID = input("Invalid, Please try again: ")
            if INVALID == "Y":
                decision = (input("What Do You Want To Change To:\n1) Set Meal\n3) Dessert\n"))
            elif INVALID == "N":
                break


    elif decision == 3:
        for yummy in dessert:
            print(yummy + "-----")
        change = input("\nIf you do not want this, please put in another number Y/N: ")
        if change == "Y":
            decision = (input("What Do You Want To Change To:\n1) Set Meal\n2) Ala Carte\n"))
            while decision != "1" and decision != "2":
                decision = input("Invalid, Please enter the correct number: ")
        elif change == "N":
            break
        else:
            INVALID = input("Invalid, Please try again: ")
            while INVALID != "Y" and INVALID != "N":
                INVALID = input("Invalid, Please try again: ")

            if INVALID == "Y":
                decision = (input("What Do You Want To Change To:\n1) Set Meal\n32) Ala Carte\n"))
            elif INVALID == "N":
                break
    else:
        decision = int(input(("Wrong Number!, Try Again!")))