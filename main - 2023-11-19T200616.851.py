def calculate_profitability(property_cost, construction_cost, rental_income):
    try:
        property_cost = float(property_cost)
        construction_cost = float(construction_cost)
        rental_income = float(rental_income)

        total_investment = property_cost + construction_cost
        annual_profit = rental_income * 12 - total_investment
        roi = (annual_profit / total_investment) * 100

        return roi
    except ValueError:
        return "Invalid input. Please enter valid numeric values."

def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Property Profitability Calculator")
    print("---------------------------------")

    property_cost = get_numeric_input("Enter the total cost of the property: $")
    construction_cost = get_numeric_input("Enter the construction cost: $")
    rental_income = get_numeric_input("Enter the potential monthly rental income: $")

    result = calculate_profitability(property_cost, construction_cost, rental_income)

    if isinstance(result, float):
        print("\nROI (Return on Investment): {:.2f}%".format(result))
    else:
        print(result)

if __name__ == "__main__":
    main()

