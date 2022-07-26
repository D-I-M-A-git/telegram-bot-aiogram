"""Функція для провідника"""
import os
import json


def file_explorer_function(way, user_id):
    """
    Файловий провідник

    :param way: Шлях у файловій системі
    :param user_id: ID користувача
    :return: Повідомлення яке має надіслати бот
    """
    global message
    if way == "back":
        with open("data.json", "w") as new_data:
            json.dump({user_id: "C:/"}, new_data)
        return [False, "Бекап зроблений!"]
    elif way == "view":
        try:
            with open("data.json", "r") as data:
                data = json.load(data)
            files = os.listdir(data[user_id])
            message = [True, [data[user_id], files]]
        except FileNotFoundError:
            message = [False, "Файл data.json не знайдений"]
        finally:
            return message
    else:
        try:
            with open("data.json", "r") as data:
                data = json.load(data)
            way += "/"
            data[user_id] += way
        except FileNotFoundError:
            return [False, "Файл data.json не знайдений"]
        try:
            files = os.listdir(data[user_id])
            with open("data.json", "w") as new_data:
                json.dump(data, new_data)
            message = [data[user_id], files]
            return [True, message]
        except FileNotFoundError:
            return [False, f'Сталась помилка!\n<{data[user_id]}>']


def get_way(user_id):
    """
    Функція для получення шляху у файловій системі
    A function to get the path in the file system

    :param user_id: Потрібно для получення шляху. Needed to get a path
    :return: шлях. Way
    """
    global way
    try:
        with open("data.json", "r") as data:
            data = json.load(data)
        way = data[user_id]
        way = [True, way]
    except FileNotFoundError:
        way = [False, "Файл data.json не знайдений"]
    finally:
        return way
