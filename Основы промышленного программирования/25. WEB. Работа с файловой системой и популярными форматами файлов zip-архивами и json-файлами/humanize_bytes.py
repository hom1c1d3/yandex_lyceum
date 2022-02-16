def human_read_format(num, suffix="Б"):
    for unit in ["", "КБ", "МБ", "ГБ", "ТБ"]:
        if abs(num) < 1024.0:
            return f"{int(num)}{unit}{suffix}"
        num /= 1024.0
    return f"{int(num)}{suffix}"


print(human_read_format(15000))