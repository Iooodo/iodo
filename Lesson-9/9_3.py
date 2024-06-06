# Даны два YAML файла (будут приложены в группе телеграмм) builds.yaml и tasks.yaml.
# В файле builds находится список “Билдов” и перечень задач для выполнение данного билда
# В файле tasks находится список задач и подзадач каждой задачи.
# 	По название Билда, необходимо вывести список задач и подзадач для выполнения билда (задачу нельзя выполнить до выполнения подзадач).

def task_subtasks(
        task_name: str,
        tasks: dict[str, list[dict[str, str | list[str]]]]
) -> list[str]:
    data = []
    for task in tasks.get("tasks"):  # type: dict
        if task.get("name") == task_name:
            for subtask in task.get("dependencies"):
                data.extend(
                    task_subtasks(task_name=subtask, tasks=tasks)
                )
            data.append(task_name)
            break
    return data


def get_build_tasks(
        build_name: str,
        builds: dict[str, list[dict[str, str | list[str]]]],
        tasks: dict[str, list[dict[str, str | list[str]]]]
) -> list[str]:
    build_tasks = []
    for build in builds.get("builds"):  # type: dict
        if build.get("name") == build_name:
            for build_task in build.get("tasks"):
                build_tasks.extend(
                    task_subtasks(task_name=build_task, tasks=tasks)
                )
            break
    return build_tasks