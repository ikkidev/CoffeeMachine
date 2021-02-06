class CoffeeMachine:
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
        },
        "off": {},
        "report": {}
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "profit": 0
    }

    def prompt_user_input(self):
        prompt_input = input("What would you like? (espresso/latte/cappuccino):")
        return prompt_input

    def is_resources_enough(self, input_drink):
        drink = self.MENU.get(input_drink)
        if drink:
            for ingredient, value in drink.get("ingredients").items():
                if self.resources.get(ingredient) < value:
                    print('Sorry there is not enough ', ingredient, '.')
                    return False

        return True

    def is_coin_enough(self, drink):
        input_coins = input("Please insert coins.\n").split(',')
        coins = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickles": 0.05,
            "pennies": 0.01
        }
        total_coin = 0.00
        for input_coin in input_coins:
            amount, coin = input_coin.split()
            total_coin += int(amount) * coins.get(coin, 0)
        round(total_coin, 2)

        drink_cost = self.MENU["espresso"]["cost"]
        if total_coin == drink_cost:
            self.resources["profit"] += drink_cost
            return True
        elif total_coin > drink_cost:
            change = round(total_coin - drink_cost, 2)
            print(change)
            print('Here is $', change, 'dollars in change')
            return True
        else:
            print("Sorry that's not enough money. Money refunded")
            return False

    def make_coffee(self, drink):
        drink_name = "espresso"
        if self.is_resources_enough(drink):
            if self.is_coin_enough(drink):
                self.use_resources(drink)
                print('Here is your', drink, '.Enjoy!\n')

        else:
            return

    def turn_on(self):
        # Ensure user inputs an item that's in our menu
        prompt_input = self.prompt_user_input()
        while prompt_input in self.MENU:
            if (prompt_input == "off"):
                exit()
            elif (prompt_input == "report"):
                self.report()
            else:
                self.make_coffee(prompt_input)

            prompt_input = self.prompt_user_input()

        print("Sorry that input is not supported")

    def use_resources(self, drink):
        for ingredient, amount in self.MENU[drink]["ingredients"].items():
            self.resources[ingredient] -= amount

    def report(self):
        for resource, value in self.resources.items():
            print(resource, ':', value, 'ml')


def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.turn_on()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
