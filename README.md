# budget-app-python

📊 Budget Manager & Spend Tracker
A robust Python-based personal finance tool that allows users to manage multiple budget categories, track deposits and withdrawals, and visualize spending habits through an ASCII-based bar chart.

🎯 User Stories
To build this application, the following user requirements were implemented:

Category Management: As a user, I want to create different budget categories (e.g., Food, Clothing, Entertainment) so I can organize my money.

Ledger Tracking: As a user, I want to deposit and withdraw money with descriptions so I have a history of my transactions.

Balance Integrity: As a user, I want the system to prevent me from withdrawing or transferring more money than I have available.

Inter-Category Transfers: As a user, I want to move funds between categories easily without manual math.

Visual Reporting: As a user, I want to see a percentage-based bar chart of my spending so I can quickly identify where my money is going.

🛠 Features
Object-Oriented Design: Utilizes a Category class to keep data and logic encapsulated.

Automated Formatting: The __str__ method automatically generates a clean, aligned receipt for any category.

Spend Analysis: The create_spend_chart function calculates the relative spending across all categories and rounds down to the nearest 10th percentile.

🚀 How to Use
1. Installation
Ensure you have Python 3.x installed. Clone this repository:

Bash
git clone https://github.com/
rishabhtrivedi9g-pixel/budget-app.git
cd budget-app
2. Running the App
You can use the Category class in your own scripts:

Python
from budget import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(105.50, "groceries")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
📈 Sample Output
Category Receipt
Plaintext
*************Food*************
initial deposit        1000.00
groceries               -10.50
Total: 989.50
Spend Chart
Plaintext
Percentage spent by category
100|          
 90|          
 80|          
 70|    o     
 60|    o     
 50|    o     
 40|    o     
 30|    o     
 20|    o  o  
 10|    o  o  o
  0| --- --- ---
     F   C   A  
     o   l   u  
     o   o   t  
     d   t   o  
         h      
🧪 Testing
The project includes a comprehensive test suite. To run the tests, use the following command:

Bash
python test_module.py
