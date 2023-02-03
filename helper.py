# -*- coding: utf-8 -*-
# test comment to push
def fileParsing(pathToFile):
    """

    :param pathToFile:
    :return:
    """
    # считывание информации из файла в массив (построчно), удаляя впереди пробелы

    with open(pathToFile, 'r') as f:
        # filedata = f.readlines()
        for line in f.readlines():
            # print(line)
            # line.lstrip()[0] == '#'
            if line.find('#') >= 0:
                print(line[0:line.find("\n")])

    # listdata = []
    #
    # for line in filedata:
    #     listdata.append(line.lstrip())
    #
    # return listdata [1:]


    # Получение списка строк комментариев из файла
def get_com_strings(file_path , com_strs):
    import os
