# Даны два YAML файла (будут приложены в группе телеграмм) builds.yaml и tasks.yaml.
# В файле builds находится список “Билдов” и перечень задач для выполнение данного билда
# В файле tasks находится список задач и подзадач каждой задачи.
# 	По название Билда, необходимо вывести список задач и подзадач для выполнения билда (задачу нельзя выполнить до выполнения подзадач).

import yaml

with open('D:/Python обучение/Lessons/builds.yaml') as fh:
    read_data = yaml.load(fh, Loader=yaml.FullLoader)
print(read_data)

with open('D:/Python обучение/Lessons/tasks.yaml') as fh:
    read_dat = yaml.load(fh, Loader=yaml.FullLoader)
# print(read_dat)