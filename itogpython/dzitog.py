#Напишите код, который запускается из командной строки и получает на вход
#путь до директории на ПК.
#Соберите информацию о содержимом в виде объектов namedtuple.
#Каждый объект хранит:
# -имя файла без расширения или название каталога,
# -расширение, если это файл,
# -флаг каталога,
# -название родительского каталога.
#В процессе сбора сохраните данные в текстовый файл используя
#логирование
import argparse
from dir_walker import dir_walker


def parse_ars():
    parser = argparse.ArgumentParser(description="hw15t01_s15t06")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директорию')
    args = parser.parse_args()
    return args.p

def main():
    path = parse_ars()[0]
    dir_walker(path, ident=0)

if __name__ == '__main__':
    main()
