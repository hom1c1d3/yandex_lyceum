import shutil
import datetime
import os


def make_reserve_arc(source, dest):
    file_name = datetime.datetime.now().isoformat().split('.')[0].replace(':', '-')
    save_path = os.path.join(dest, file_name)
    archive_format = 'zip'
    shutil.make_archive(save_path, archive_format, source)


def main():
    archive_path = input('Что архивируем: ')
    if not os.path.exists(archive_path):
        print(f'"{archive_path}" не существует!')
        return 1
    save_path = input('Куда сохранять: ')
    if not os.path.exists(save_path):
        print(f'"{save_path}" не существует!')
        return 1
    make_reserve_arc(archive_path, save_path)
    print('Готово')
    return 0


if __name__ == '__main__':
    exit(main())