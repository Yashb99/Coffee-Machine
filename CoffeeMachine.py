from string import punctuation


class CoffeeMachine:
    def __init__(self, water_amount, milk_amount, coffee_amount, disposable_cups, amount):
        self.water_amount = water_amount
        self.milk_amount = milk_amount
        self.coffee_amount = coffee_amount
        self.disposable_cups = disposable_cups
        self.amount = amount
        self.regex = punctuation
        self.current_state = 'Choosing an action'

    def action(self):
        wrong = True
        while wrong:
            while True:
                usage = input('Write action (buy, fill, take, remaining, exit) :\n')
                if any(c in self.regex for c in usage) or not usage or usage.isnumeric():
                    print('Please enter a valid value.\n')
                    continue
                elif usage != 'buy' and usage != 'fill' and usage != 'take' and usage != 'remaining' and usage != 'exit':
                    print('Please enter a valid value.\n')
                    continue
                try:
                    if usage == 'buy':
                        self.buy()
                    elif usage == 'fill':
                        self.fill()
                    elif usage == 'take':
                        self.take()
                    elif usage == 'remaining':
                        self.remaining()
                    elif usage == 'exit':
                        break
                except ValueError:
                    print('Please enter a valid value.\n')
                    continue

                wrong = False
            if wrong:
                break

    def espresso(self):
        while True:
            if self.water_amount < 250:
                print('Sorry, not enough water!\n')
                break
            elif self.coffee_amount < 16:
                print('Sorry, not enough coffee beans!\n')
                break
            elif self.disposable_cups < 1:
                print('Sorry, not enough disposable cups!\n')
                break
            else:
                print('I have enough resources, making you a coffee!\n')
                self.water_amount -= 250
                self.coffee_amount -= 16
                self.amount += 4
                self.disposable_cups -= 1
                break

    def latte(self):
        while True:
            if self.water_amount < 350:
                print('Sorry, not enough water!\n')
                break
            elif self.milk_amount < 75:
                print('Sorry, not enough milk!\n')
                break
            elif self.coffee_amount < 20:
                print('Sorry, not enough coffee beans!\n')
                break
            elif self.disposable_cups < 1:
                print('Sorry, not enough disposable cups!\n')
                break
            else:
                print('I have enough resources, making you a coffee!\n')
                self.water_amount -= 350
                self.coffee_amount -= 20
                self.amount += 7
                self.disposable_cups -= 1
                break

    def cappuccino(self):
        while True:
            if self.water_amount < 200:
                print('Sorry, not enough water!\n')
                break
            elif self.milk_amount < 100:
                print('Sorry, not enough milk!\n')
                break
            elif self.coffee_amount < 20:
                print('Sorry, not enough coffee beans!\n')
                break
            elif self.disposable_cups < 1:
                print('Sorry, not enough disposable cups!\n')
                break
            else:
                print('I have enough resources, making you a coffee!\n')
                self.water_amount -= 350
                self.coffee_amount -= 20
                self.amount += 7
                self.disposable_cups -= 1
                break

    def buy(self):
        new = True
        while new:
            c_type = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
            if any(c in self.regex for c in c_type) or not c_type or c_type.isalpha() and c_type != 'back':
                print('Please enter a valid input.')
                continue
            elif c_type != '1' and c_type != '2' and c_type != '3' and c_type != 'back' or c_type.isnumeric() > 3:
                print('Please choose from the espresso, latte and capuccino only.')
                continue
            try:
                if c_type == '1':
                    self.espresso()
                elif c_type == '2':
                    self.latte()
                elif c_type == '3':
                    self.cappuccino()
                elif c_type == 'back':
                    self.action()
            except ValueError:
                print('Please enter a valid input\n')
                continue

            new = False

    def fill(self):
        elf = True
        while elf:
            water = input('\nWrite how many ml of water you want to add:\n')
            if any(c in self.regex for c in water) or not water or water.isalpha():
                print('Please enter a valid value.')
                continue
            elif any(x.isalpha() for x in water) and any(x.isnumeric() for x in water):
                print('Please enter a valid value.')
                continue
            milk = input('Write how many ml of milk you want to add:\n')
            if any(c in self.regex for c in milk) or not milk or milk.isalpha():
                print('Please enter a valid value.')
                continue
            elif any(x.isalpha() for x in milk) and any(x.isnumeric() for x in milk):
                print('Please enter a valid value.')
                continue
            beans = input('Write how many grams of coffee beans you want to add:\n')
            if any(c in self.regex for c in beans) or not beans or beans.isalpha():
                print('Please enter a valid value.')
                continue
            elif any(x.isalpha() for x in beans) and any(x.isnumeric() for x in beans):
                print('Please enter a valid value.')
                continue
            cups = input('Write how many disposable coffee cups you want to add:\n')
            if any(c in self.regex for c in cups) or not cups or cups.isalpha():
                print('Please enter a valid value.')
                continue
            elif any(x.isalpha() for x in cups) and any(x.isnumeric() for x in cups):
                print('Please enter a valid value.')
                continue
            try:
                self.water_amount += int(water)
                self.milk_amount += int(milk)
                self.coffee_amount += int(beans)
                self.disposable_cups += int(cups)
            except ValueError:
                print('Please enter a valid value.\n')
                continue

            elf = False

    def take(self):
        money = 0
        money += self.amount
        self.amount = 0
        print(f'\nI gave you {money}')
        print('')

    def remaining(self):
        print(f'''\nThe coffee machine has: 
{self.water_amount} ml of water 
{self.milk_amount} ml of milk     
{self.coffee_amount} g of coffee beans
{self.disposable_cups} of disposable cups
${self.amount} of money \n''')


def main():
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    machine.action()


if __name__ == '__main__':
    main()
