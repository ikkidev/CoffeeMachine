def check_transaction():
    pass


def make_coffee():
    pass


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

    def switch(self, prompt_input):
        # Ensure user inputs an item that's in our menu
        while prompt_input in self.MENU:
            getattr(self, prompt_input, lambda: "off")()
            prompt_input = self.prompt_user_input()

    def is_coin_enough(self, drink):
        input_coins = input("Please insert coins").split(',')
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

    def is_resources_enough(self, input_drink):
        drink = self.MENU.get(input_drink)
        if drink:
            for ingredient, value in drink.get("ingredients").items():
                if self.resources.get(ingredient) < value:
                    print('Sorry there is not enough ', ingredient, '.')
                    return False

        return True

    def espresso(self):
        drink_name = "espresso"
        if self.is_resources_enough(drink_name):
            coin = self.is_coin_enough(drink_name)

        else:
            return

    def latte(self):
        pass

    def cappucino(self):
        pass

    def report(self):
        for resource, value in self.resources.items():
            print(resource, ':', value, 'ml')

    def off(self):
        exit()


def main():
    coffee_machine = CoffeeMachine()
    prompt_input = coffee_machine.prompt_user_input()
    coffee_machine.switch(prompt_input)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
