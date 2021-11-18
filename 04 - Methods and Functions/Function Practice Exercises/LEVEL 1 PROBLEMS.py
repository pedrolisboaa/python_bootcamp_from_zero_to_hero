"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""


def old_macdonald(name):
    new_name = name.capitalize()
    return new_name.replace(name[3], name[3].upper(), 1)


print(old_macdonald('macdonald'))
print(old_macdonald('pedro'))
print('*'*30)

"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
"""


def master_yoda(text):
    new_text = text.split()
    new_text_reverse = []
    for i in new_text[::-1]:
        new_text_reverse.append(i)
    x = ' '.join(new_text_reverse)
    return x


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
