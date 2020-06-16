class CoffeeMachine:
    running = False
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk   
        self.coffee = coffee
        self.cups = cups
        self.money = money 
        if not self.running:
            self.coffee_mode()
    
    def get_input(self):
        return input()
        
        
    def machine_status(self):
        print(f"""The coffee machine has:
    {self.water} of water
    {self.milk} of milk
    {self.coffee} of coffee beans
    {self.cups} of disposable cups
    {self.money} of money\n
    """)

    def coffee_mode(self):
        running = True
        while running:
            print("Write action (buy, fill, take, remaining, exit):\n")
            action = self.get_input()
            if action == "buy":
                print()
                self.buy()
                print()
            if action == "fill":
                self.fill()
                print()
            if action == "take":
                self.take()
                print()
            if action == "remaining":
                self.machine_status()
                print()
            if action == "exit":
                running = False
                break
            
    def take(self):
        self.money = 0

    def fill(self):  
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        n = self.get_input()
        if n == "back":
            return
        if n == "1":
            self.make_coffee(16, 250, 0, 1, 4)
        if n == "2":
            self.make_coffee(20, 350, 75, 1, 7)
        if n == "3":
            self.make_coffee(12, 200, 100, 1, 6)
    def check_resources(self, cof, w, m, c):
           
        if cof > self.coffee:
            print("Sorry, not enough coffee!")
            return False
        if w > self.water:
            print("Sorry, not enough water!")
            return False
        if m > self.milk:
            print("Sorry, not enough milk!")
            return False
        if c > self.cups:
            print("Sorry, not enough cups!")
            return False
        return True
        
        print("I have enough resources, making you a coffee!") 
        
    def make_coffee(self, cof, w, m, c, cost):
    
        if self.check_resources(cof, w, m, c):
            self.cups -= c
            self.water -= w
            self.milk -= m
            self.coffee -= cof
            self.money += cost
          
CoffeeMachine(400, 540, 120, 9, 550)

