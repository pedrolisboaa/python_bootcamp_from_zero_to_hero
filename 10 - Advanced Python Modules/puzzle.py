"""
Zip realizado
from zipfile import ZipFile
z = ZipFile('unzip_me_for_instructions.zip', 'r')
z.extractall()
z.close()
"""

import re
import os
patter = r'\d{3}-d{3}-d{4}'


def search(file, pattern=r'\d{3}-d{3}-d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


results = []
for pastas, sub_pastas, arquivos in os.walk('extracted_content'):
    for f in arquivos:
        full_path = pastas + '\\' + f

        results.append(search(full_path))

print(results)