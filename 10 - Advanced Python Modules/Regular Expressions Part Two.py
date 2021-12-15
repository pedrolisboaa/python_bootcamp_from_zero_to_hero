import re

text = 'My phone number is 61 99147-8523'
phone = re.search(r'\d{2} \d{5}-\d{4}', text)
print(phone.group())