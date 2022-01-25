class CoffeeMachine:

    running = False
    
    def __init__(self, water, milk, coffee_beans, cups, money):
        # quantities of items the coffee machine already had
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
        
        #if the machine isnt running then start running
        if not CoffeeMachine.running:
            self.start()

    def start(self):
        self.running = True # it is running as to not trigger the start() in initialiser method
        print("Welcome to GREAT DAY Coffee machine!")
        self.action = int(input("Choose action to perform:\n1--I WANT TO BUY COFFEE\n2--I WANT A REPORT OF MY COFFEE\n3--I WANT TO SEE THE STATUS OF MACHINE\n4--OFF: "))
        #possible choices to perform in the coffee machine
        action_choices = {1: self.buy, 2: self.report,4: exit,3: self.status}
        if self.action in action_choices:
            action_choices[self.action]()
        else:
            exit()

    def return_to_menu(self): # returns to the menu after an action
        print()
        self.start()
   

    def available_check(self): # checks if it can afford making that type of coffee at the moment
        self.not_available = "" # by checking whether the supplies goes below 0 after it is deducted
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee_beans - self.reduced[2] < 0:
            self.not_available = "coffee beans"
        elif self.cups - self.reduced[3] < 0:
            self.not_available = "disposable cups"
        
        if self.not_available != "": # if something was detected to be below zero after deduction
            print(f"Sorry, not enough {self.not_available}!")
            return False
        else: # if everything is enough to make the coffee
            print("I have enough resources, making you a coffee!")
            return True

    def deduct_supplies(self): # performs operation from the reduced list, based on the coffee chosen
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee_beans -= self.reduced[2]
        self.cups -= self.reduced[3]
        self.money += self.reduced[4]

    def buy(self):#buying the coffee of choice
        self.choice = input("What do you want to buy?\n1 - Espresso\n2 - Latte\n3 - Cappuccino\n4 - back to main menu:\n")
        if self.choice == '1':
            self.reduced = [250, 0, 16, 1, 4] # water, milk, coffee beans, cups, money
            if self.available_check(): # checks if supplies are available
                self.deduct_supplies() # if it is, then it deducts

        elif self.choice == '2':
            self.reduced = [350, 75, 20, 1, 7]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "3":
            self.reduced = [200, 100, 12, 1, 6]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "4": # if the user changed his mind
            self.return_to_menu()

        self.take()

    def report(self): # for user's report of ingredients
        print("Your coffee has")
        print("Water:",self.reduced[0],"ml")
        print("Milk:",self.reduced[1],"ml")
        print("Coffee-beans",self.reduced[2],"nos.")
        print("Cost:$",self.reduced[4])
        self.return_to_menu()

    def take(self): # for paying the amount
        print("The Cost is:$",self.reduced[4])
        print("Please insert coins.")
        quarters=int(input("enter the number of quarters(0.25)")) #for calculating quarters
        dimes=int(input("enter the number of dimes(0.10)"))       #for calculating dimes
        nickels=int(input("enter the number of nickels(0.50)"))   #for calculating nickels
        pennies=int(input("enter the number of pennies(0.01)"))   #for calculating pennies
        amt=quarters*0.25+dimes*0.1+nickels*0.5+pennies*0.01      #calculating total inserted
        print(f"You gave: $",amt)
        if(amt==self.reduced[4]):
            print("yay!Order confirmed.")
        elif(amt!=self.reduced[4]):
            if(amt>self.reduced[4]):
               print("Balance amount:$",amt-self.reduced[4])
               print("Collect your balance")
               print("yay!Order confirmed.")
            elif(amt<self.reduced[4]):
               print("Paid amount is not enough!\npay balance $",self.reduced[4]-amt)
               print("insert coins:")
               quarters=int(input("enter the number of quarters(0.25)"))
               dimes=int(input("enter the number of dimes(0.10)"))
               nickels=int(input("enter the number of nickels(0.50)"))
               pennies=int(input("enter the number of pennies(0.01)"))
               if(quarters*0.25+dimes*0.1+nickels*0.5+pennies*0.01==self.reduced[4]-amt):
                   print("yay!Order confirmed.")
        print("Here's your Order. Enjoy!\n Have a great day with coffee ;)")
        self.return_to_menu()

    def status(self): # to display the quantities of supplies in the machine at the moment
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        self.return_to_menu()

CoffeeMachine(800, 940, 120, 50, 1000) # specify the quantities of supplies at the beginning
            # water, milk, coffee beans, disposable cups, money
