def user_choice():
    choice = 'WRONG'
    acceptable_range = range(0, 10)
    within_range = False

    while not choice.isdigit() or not within_range:
        choice = input('Please enter a number (0-10) ')

        if not choice.isdigit():
            print(f'Sorry that is not a digit!')

        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print(f'Sorry, you are out of acceptable range (0-10)')
                within_range = False
    return int(choice)


print(user_choice())
