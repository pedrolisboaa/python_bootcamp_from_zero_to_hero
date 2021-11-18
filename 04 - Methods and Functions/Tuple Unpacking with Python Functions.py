stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for ticker, price in stock_prices:
    print(price)


word_hours = [('Pedro', 200), ('Marcelo', 300), ('Maria', 350)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return employee_of_month, current_max


teste = employee_check(word_hours)
print(teste)