import json
import os
from pprint import pprint

id = 0
def add_car(id):
    '''Yangi mashina qo'shadigan funksiya,
    Ushbu funksiyaga har safar murojat qilganimizda 1ta mashina haqida ma'lumot qo'shadi'''
    model = input('Model: ')
    brand = input('Brand: ')
    year = input('Year: ')
    price = int(input('Price: '))
    active = bool(input('Active: '))
    automat = bool(input('Automat: '))
    car = {
        'id': id,
        'model': model,
        'brand': brand,
        'year': year,
        'price': price,
        'active': active,
        'automat': automat
    }
    while True:
        if os.path.exists('cars.json'):
            break
        with open('cars.json', 'w') as file:
            json.dump([], file, indent=4)
    all_data = show_cars()
    all_data.append(car)
    with open('cars.json', 'w') as file:
        json.dump(all_data, file, indent=4)
        print('Mashina bazaga kiritildi')

def show_cars():
    with open('cars.json') as file:
        data = json.load(file)
        return data

while True:
    id += 1
    try:
        add_car(id)
    except ValueError:
        print('Mashinani xato kiritdingiz')
        id -= 1
    play = input('yana kiritasizmi(ha/yo\'q): ')
    if play != 'ha':
        break

def show_car(id_car):
    car = show_cars()[id_car - 1]
    return car

while True:
    try:
        id_car = int(input('Qaysi id li mashinani qidiryapsiz: '))
    except ValueError:
        print('Xato kiritdingiz!')
        continue
    if id_car > len(show_cars()) or id_car <= 0:
        try:
            id_car = int(input('Bunday id li mashina yo\'q, qayta kiriting: '))
        except ValueError:
            print('Xato kiritdingiz!')
    else:
        break

pprint(show_car(id_car))
