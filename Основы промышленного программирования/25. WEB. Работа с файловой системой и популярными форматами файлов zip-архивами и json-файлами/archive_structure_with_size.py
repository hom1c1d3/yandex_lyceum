from zipfile import ZipFile


def human_read_format(num_bytes):
    for unit in ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПТ"]:
        next_format = num_bytes / 1024
        if next_format < 1:
            return str(num_bytes) + unit
        else:
            num_bytes = round(next_format)


with ZipFile('input.zip') as myzip:
    for file in myzip.infolist():
        file_name = file.filename.rstrip('/').split('/')
        if file.is_dir():
            file_size_humanized = ''
        else:
            file_size_humanized = human_read_format(file.file_size)
            file_size_humanized = ' ' + str(file_size_humanized)
        print("  " * (len(file_name) - 1) + file_name[-1] + file_size_humanized)
