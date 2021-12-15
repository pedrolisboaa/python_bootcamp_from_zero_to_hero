import re

text = "The agent's phone number is 61 99147-6760. Call soon!"

patter = 'phone'

print(re.search(patter, text))
print(re.findall('phone', text))