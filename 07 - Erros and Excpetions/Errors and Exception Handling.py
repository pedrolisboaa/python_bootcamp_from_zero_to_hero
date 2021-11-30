# def add(n1, n2):
#     print(n1 + n2)
#
#
# try:
#     result = 10 + '10'
#
# except:
#     print('Error!')
# else:
#     print('Something happened!')
#     print(result)

# try:
#     f = open('testfile', 'r')
#     f.write('Write a teste line')
# except TypeError:
#     print(f'There was a type error')
# except Exception as e:
#     print(f'Hey you have ', e)
# finally:
#     print('I always run')

def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops! Tha is not a number: ')
            continue
        else:
            print('Yes thank you')
            print(result)
            break
        finally:
            print(f'End of try/except/finaly')


ask_for_int()