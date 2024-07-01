# Hardcoded exchange rates (example rates, not real-time)
exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0, 'INR': 74.0},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'JPY': 130.0, 'INR': 87.0},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 148.0, 'INR': 98.0},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0067, 'INR': 0.66},
    'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.010, 'JPY': 1.52},
}

def convert(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        exchange_rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        raise ValueError("Invalid currency code or conversion not available.")

def main():
    print("Welcome to the Currency Converter")
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the from currency (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the to currency (e.g., USD, EUR, GBP): ").upper()

    try:
        converted_amount = convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)

if name == "main":
    main()