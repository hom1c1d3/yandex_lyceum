def human_read_format(num_bytes):
    for unit in ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПТ"]:
        next_format = num_bytes / 1024
        if next_format < 1:
            return str(num_bytes) + unit
        else:
            num_bytes = round(next_format)


print(human_read_format(15000))
