class BillSplitter:
    def __init__(self):
        self.people = ["Yulisma", "Harry", "Marko", "Virgo"]
        self.expenses = []
        self.subtotal = 0
        self.month = None
        self.year = None

    def set_month_and_year(self):
        """Prompt for numerical month and year once at the start of the session."""
        while True:
            try:
                self.month = int(input("Enter the month for the bills (1-12): "))
                if 1 <= self.month <= 12:
                    break
                else:
                    print("Please enter a valid month between 1 and 12.")
            except ValueError:
                print("Invalid input. Please enter a number for the month.")

        self.year = input("Enter the year for the bills (e.g., 2024): ")

    def add_fixed_expenses(self):
        """Add fixed expenses paid by Yulisma."""
        print("\nAdding fixed expenses...\n")

        # Rent
        rent_split = {"Yulisma": 850, "Harry": 0, "Marko": 795, "Virgo": 755}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "Rent",
            "amount": 2400,
            "split_amount": rent_split
        })
        
        # Octopus Energy
        octopus_split = {person: 150.56 / 4 for person in self.people}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "Octopus Energy",
            "amount": 150.56,
            "split_amount": octopus_split
        })

        # Thames Water
        thames_split = {person: 45 / 4 for person in self.people}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "Thames Water",
            "amount": 45,
            "split_amount": thames_split
        })

        # TV License
        tv_license_split = {"Yulisma": 13.25, "Harry": 0, "Marko": 0, "Virgo": 0}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "TV License",
            "amount": 13.25,
            "split_amount": tv_license_split
        })

        # Council Tax
        council_tax_split = {"Yulisma": 231 / 3, "Harry": 0, "Marko": 231 / 3, "Virgo": 231 / 3}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "Council Tax",
            "amount": 231,
            "split_amount": council_tax_split
        })

        # Sky Internet and Netflix
        sky_netflix_split = {person: 38 / 4 for person in self.people}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "Sky Internet and Netflix",
            "amount": 38,
            "split_amount": sky_netflix_split
        })

        # Ring Doorbell Subscription
        ring_doorbell_split = {person: 5 / 4 for person in self.people}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "Ring Doorbell Subscription",
            "amount": 5,
            "split_amount": ring_doorbell_split
        })

        # Denplan Insurance (only for Marko)
        denplan_split = {"Yulisma": 0, "Harry": 0, "Marko": 45, "Virgo": 0}
        self.expenses.append({
            "payer": "Yulisma",
            "month": self.month,
            "year": self.year,
            "description": "Denplan Insurance",
            "amount": 45,
            "split_amount": denplan_split
        })

        # Update subtotal
        fixed_expenses_total = 2400 + 150.56 + 45 + 13.25 + 231 + 38 + 5 + 45
        self.subtotal += fixed_expenses_total
        print(f"Fixed expenses added. Subtotal of fixed expenses: £{fixed_expenses_total:.2f}\n")

    def add_expense(self):
        """Add individual expense without asking for month and year again."""
        while True:
            # Get bill details
            payer = input("Who paid the bill? (Yulisma/Harry/Marko/Virgo): ")
            while payer not in self.people:
                payer = input("Invalid payer. Please choose from Yulisma/Harry/Marko/Virgo: ")

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
            print(f"Month/Year: {self.month}/{self.year}")
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
                    "month": self.month,
                    "year": self.year,
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
            print(f"\n{expense['description']} - {expense['month']}/{expense['year']}: £{expense['amount']}")
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

    def display_full_summary(self):
        """Display final totals and who owes whom."""
        self.display_expenses()
        print("\nFinal breakdown for each person:")
        balances = self.calculate_balances()

        for person in self.people:
            print(f"\n{person}'s expense breakdown:")
            total_owed = 0
            for expense in self.expenses:
                if expense['split_amount'][person] > 0:
                    print(f"{expense['description']}: £{expense['split_amount'][person]:.2f}")
                    total_owed += expense['split_amount'][person]
            print(f"Total for {person}: £{total_owed:.2f}")
            if balances[person] > 0:
                print(f"{person} is owed £{balances[person]:.2f}")
            elif balances[person] < 0:
                print(f"{person} owes £{-balances[person]:.2f}")
            else:
                print(f"{person} is settled up.")

# Main application flow
if __name__ == "__main__":
    splitter = BillSplitter()

    # Set month and year once at the beginning of the session
    print("\n--- Bill Splitter ---")
    splitter.set_month_and_year()

    # Add fixed expenses paid by Yulisma
    splitter.add_fixed_expenses()

    # Ask if the user wants to add additional expenses
    more_bills = input("All fixed expenses have been added. Do you want to add additional expenses? (yes/no): ")

    if more_bills.lower() == "yes":
        while True:
            splitter.add_expense()
            
            more_bills = input("Do you want to add another bill? (yes/no): ")
            if more_bills.lower() != "yes":
                break

    # Display full summary
    splitter.display_full_summary()