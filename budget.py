class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"

        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += desc + amt + "\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    
    # Calculate spending and percentages
    spendings = [sum(-item['amount'] for item in c.ledger if item['amount'] < 0) for c in categories]
    total_spent = sum(spendings)
    # Round down to nearest 10
    percentages = [int((s / total_spent) * 10) * 10 for s in spendings]

    # Build the Y-axis and bars
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # Dash line (4 spaces, then 3 dashes per category + 1 extra dash)
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Vertical Names
    max_len = max(len(c.name) for c in categories)
    names = [c.name.ljust(max_len) for c in categories]
    
    for i in range(max_len):
        chart += "     " # 5 spaces to align with the first 'o'
        for name in names:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"

    return chart
