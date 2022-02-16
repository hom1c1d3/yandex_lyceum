from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    for file in myzip.namelist():
        file = file.rstrip('/').split('/')
        print("  " * (len(file) - 1) + file[-1])