import os


def human_read_format(num_bytes):
    for unit in ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПТ"]:
        next_format = num_bytes / 1024
        if next_format < 1:
            return str(num_bytes) + unit
        else:
            num_bytes = round(next_format)


def get_path_size(path):
    if os.path.isfile(path):
        return path, os.path.getsize(path)
    else:
        return path, sum(get_path_size(os.path.join(path, i))[1] for i in os.listdir(path))


def main():
    path = '../../Основы промышленного программирования'
    infos = []
    for file_path in os.listdir(path):
        _, file_size = get_path_size(os.path.join(path, file_path))
        infos.append((file_path, file_size))
    infos = sorted(infos, key=lambda x: x[1], reverse=True)
    infos = infos[:10]
    infos = [(path, human_read_format(size)) for path, size in infos]
    max_path_length = max(len(i[0]) for i in infos)
    max_size_length = max(len(i[1]) for i in infos)
    for path, size in infos:
        print(path.ljust(max_path_length) + ' ' * 4, '-', size.rjust(max_size_length))


if __name__ == '__main__':
    main()