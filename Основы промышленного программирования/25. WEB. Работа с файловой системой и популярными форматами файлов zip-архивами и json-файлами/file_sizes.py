# import os
#
#
# def human_read_format(num_bytes):
#     for unit in ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПТ"]:
#         if num_bytes / 1024 < 1.0:
#             return str(int(num_bytes)) + unit
#         else:
#             num_bytes = round(num_bytes / 1024)
#
#
# def get_files_sizes():
#     parent_dir = os.getcwd()
#     res = ''
#     for cur_dir, dirs, files in os.walk(parent_dir):
#         for file_name in files:
#             try:
#                 size = human_read_format(os.path.getsize(parent_dir + '/' + file_name))
#                 res += (file_name + ' ' + size + '  \n')
#             except Exception:
#                 pass
#     return res
#
#
# print(get_files_sizes())


import os


def human_read_format(size):
    units = ['Б', 'КБ', 'МБ', 'ГБ']
    for unit in units:
        if size / 1024 < 1:
            return f'{int(size)}{unit}'
        size = round(size / 1024)


def get_files_sizes():
    parent_dir = os.getcwd()
    total = ''
    for cur_dir, dirs, files in os.walk(parent_dir):
        for file_name in files:
            try:
                size = human_read_format(os.path.getsize(parent_dir + '/' + file_name))
                total += (file_name + ' ' + size + '\n')
            except Exception:
                pass
    return total

