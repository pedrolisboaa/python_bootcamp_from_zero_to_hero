"""
LAUGHTER: Write a function that counts the number of times a given pattern appears in a string, including overlap
"""


def laughter(pattern, text):
    return text.count(pattern)


print(laughter('hah', 'hahahah'))
print(laughter('pepe', 'pepelisboapepelisboapeppepelisboa'))


"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
"""


def paper_doll(text):
    new = []
    for i in text:
        new.append(i*3)
    new_text = ''.join(new)
    return new_text


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

