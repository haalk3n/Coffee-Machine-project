# Coffee-Machine-project
Python Project that utilizes Dictionaries, defining functions, checking conditions, remembering values, calling functions with parameters.

This is a project made by following these requirements:
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

2. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

3. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.

4. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values.

5. When the user chooses a drink, the program should check if there are enough
resources to make that drink.

6. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.

7. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 1 dime, 1 nickel, 1
penny = 0.25 + 0.1 x 1 + 0.05 + 0.01 x 1 = $0.41

8. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.41 then after counting the coins the
program should say "You have not inserted enough money. Money returned.".

9. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered.

10. If the user has inserted too much money, the machine should offer change.

11. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
