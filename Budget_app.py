class Category:
    def __init__(self, name):
        self.name = name
        #created empty llist to store transaction
        self.ledger = []
#add money into category
    def deposit(self, amount, description=""):
        #Add transaction into ledger
        self.ledger.append({
            "amount": amount,
            "description": description
        })
#Removes money
    def withdraw(self, amount, description=""):
        #check if enough money exist
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            #means withdraw successful
            return True
        #means not enough money
        return False
#Calculate current balance
    def get_balance(self):
        total = 0
        for item in self.ledger:     
            total += item["amount"]
        return total
#Send money from one category to another
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")#Withdraw from current category.
            category.deposit(amount, f"Transfer from {self.name}")#Deposit into other category.
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
#loop through transaction
        for item in self.ledger:
            desc = item["description"][:23]#Takes only 23 letters
            amt = f"{item['amount']:.2f}"[:7]#Formats amount to 2 decimal places.
            items += f"{desc:<23}{amt:>7}\n"

        total = f"Total: {self.get_balance()}"#Shows final balance.
        return title + items + total#Returns full printable text.


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    spent = []#spent stores each category spending
    total_spent = 0#total_spent stores all spending

    for category in categories:#Go category by category.
        amount = 0#Reset spending count.
        for item in category.ledger:
            if item["amount"] < 0:
                amount += -item["amount"]#Negative becomes positive spending.
        spent.append(amount)
        total_spent += amount
#Conver  to percentage
    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 10) * 10
        percentages.append(percent)
#Build Chart Bars
    chart = title

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i != max_len - 1:
            chart += "\n"

    return chart
food = Category("Food")
food.deposit(1000)
food.withdraw(200)

cloth = Category("Clothing")
cloth.deposit(500)
cloth.withdraw(100)

print(food)
print(create_spend_chart([food, cloth]))