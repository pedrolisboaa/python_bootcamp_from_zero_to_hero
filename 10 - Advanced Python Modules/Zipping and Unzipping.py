import zipfile

com_file = zipfile.ZipFile('arquivos_zipados', 'w')
com_file.write('arqruivo_para_zip.txt', compress_type=zipfile.ZIP_DEFLATED)
com_file.write('arqruivo_para_zip2.txt', compress_type=zipfile.ZIP_DEFLATED)

com_file.close()

