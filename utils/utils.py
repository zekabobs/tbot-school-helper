import csv
import os


def get_info():
    with open('files/docs/info_main.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def get_sticker_hello():
    with open('files/stickers/sticker_hello.webp', 'rb') as f:
        sticker = f.read()
    return sticker


def generate_events():
    events_list = os.listdir('files/event/')[-1]
    if events_list:
        return open('files/event/' + events_list, 'rb').read()
    else:
        return None


def get_timetable(class_='general'):
    path = 'files/timetable/' + class_

    if os.path.exists(path):
        return open(path + '/' + os.listdir(path)[-1], 'rb').read()
    return None


def generate_menu(text={'первое', 'второе', 'напитки'}):
    response = ''
    for item in text:
        response += get_menu(item)

    if not response:
        response = 'Некорректный запрос 😣😣😣'
    return response


def get_menu(item):
    if os.listdir('files/menu/').count(item + '.csv'):
        result = '<b>' + item.upper() + '</b>' + '\n'
        with open('files/menu/' + f'{item}.csv', 'r', encoding='utf-8') as f:
            data = csv.reader(f)
            for row in data:
                if bool(row[3]):
                    result += '<b>{}:</b>\t <u>{}</u>\n'.format(row[1], row[2])
        return result + '\n'
    return ''