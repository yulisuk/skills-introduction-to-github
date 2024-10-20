class BillSplitter:
    def __init__(self):
        self.people = ["Yulisma", "Harry", "Marko", "Virgo"]
        self.expenses = []
        self.subtotal = 0

    def add_expense(self):
        while True:
            # Get bill details
            payer = input("Who paid the bill? (Yulisma/Harry/Marko/Virgo): ")
            while payer not in self.people:
                payer = input("Invalid payer. Please choose from Yulisma/Harry/Marko/Virgo: ")

            month = input("Enter the month for the bill (e.g., January): ")
            year = input("Enter the year for the bill (e.g., 2024): ")
            description = input("Enter a description of the bill (e.g., Rent): ")
            amount = float(input(f"Enter the total amount for {description}: £"))

            # Check if the bill is to be split equally or customised
            split_type = input("Is the bill split equally or customised? (equal/custom): ")

            if split_type.lower() == "equal":
                split_amount = {person: amount / 4 for person in self.people}
            else:
                split_amount = {}
                print("Enter the custom amount for each person:")
                for person in self.people:
                    split_amount[person] = float(input(f"Amount for {person}: £"))

            # Display the entered expense for verification
            print(f"\nYou've entered the following expense:")
            print(f"Description: {description}")
            print(f"Month/Year: {month} {year}")
            print(f"Total Amount: £{amount:.2f}")
            print(f"Paid by: {payer}")
            if split_type.lower() == "equal":
                print("Split equally among all:")
            else:
                print("Custom split amounts:")

            for person, share in split_amount.items():
                print(f"{person} owes: £{share:.2f}")

            # Prompt for verification
            correct = input("Is this information correct? (yes/no): ")
            if correct.lower() == "yes":
                # Store the expense
                self.expenses.append({
                    "payer": payer,
                    "month": month,
                    "year": year,
                    "description": description,
                    "amount": amount,
                    "split_amount": split_amount
                })
                self.subtotal += amount
                break
            else:
                print("Let's re-enter the details.")

        # Show the current subtotal after adding the expense
        print(f"\nCurrent Subtotal of all added expenses: £{self.subtotal:.2f}\n")

    def calculate_balances(self):
        balances = {person: 0 for person in self.people}

        # Calculate how much each person owes or is owed
        for expense in self.expenses:
            payer = expense['payer']
            for person, share in expense['split_amount'].items():
                if person == payer:
                    balances[payer] += (expense['amount'] - share)  # The payer should receive the remainder
                else:
                    balances[person] -= share  # Others owe their share

        return balances

    def display_expenses(self):
        print("\nDetailed breakdown of expenses:")
        for expense in self.expenses:
            print(f"\n{expense['description']} - {expense['month']} {expense['year']}: £{expense['amount']}")
            for person, share in expense['split_amount'].items():
                print(f"{person} owes: £{share:.2f}")
            print(f"Paid by: {expense['payer']}")

    def display_balances(self):
        balances = self.calculate_balances()
        print("\nFinal balance summary:")
        for person, balance in balances.items():
            if balance > 0:
                print(f"{person} is owed £{balance:.2f}")
            elif balance < 0:
                print(f"{person} owes £{-balance:.2f}")
            else:
                print(f"{person} is settled up.")

# Main application flow
if __name__ == "__main__":
    splitter = BillSplitter()

    while True:
        print("\n--- Bill Splitter ---")
        splitter.add_expense()
        
        more_bills = input("Do you want to add another bill? (yes/no): ")
        if more_bills.lower() != "yes":
            break

    splitter.display_expenses()
    splitter.display_balances()