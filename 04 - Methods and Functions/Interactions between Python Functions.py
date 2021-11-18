def shuffle_list(mylist):
    from random import shuffle
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1 or 2: ')

    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == '0':
        print(mylist)
        print('Correct!')
    else:
        print(f'Wrog guess!')
        print(mylist)


if __name__ == '__main__':
    print([' ', '0', ' '])
    # INITIAL LIST
    mylist = [' ', '0', ' ']
    # SHUFFLE LIST
    shuffle = shuffle_list(mylist)
    # USER GUESS
    guess = player_guess()
    # CHECK GUESS
    check_guess(shuffle, guess)
