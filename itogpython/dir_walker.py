from collections import namedtuple
import os
from common_log_util import common_log

FSObject = namedtuple('FSObject', 'name ext is_dir parent', defaults=['', '', False, ''])   # (имя файла, расширение, директория или нет, родительская директория) - кортеж
fs_objects = []


def dir_walker(path, ident):
    for item in os.listdir(path):

        # метод os.path.join(path, itemName) создаёт полнуй путь объекта item
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            # это директория, делаем что-то с этим, и потом заходим в неё рекурсивно
            # --------------------
            # do something
            fsi = FSObject(name=item_path, ext=None, parent=path, is_dir=True)
            fs_objects.append(fsi)
            common_log.info(f"{' ' * ident} {fsi}")
            # --------------------
            dir_walker(item_path, ident + 4)
        else:
            # это файл... делаем что-то с этим
            # --------------------
            # do something
            fileName, fileExt = os.path.splitext(item_path)
            fsi = FSObject(name=fileName, ext=fileExt, parent=path, is_dir=False)
            fs_objects.append(fsi)
            common_log.info(f"{' ' * ident} {fsi}")
            # --------------------


if __name__ == '__main__':
    print('Not for separate use')
