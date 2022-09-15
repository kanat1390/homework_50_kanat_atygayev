from random import randint
from ..database.database import Cat, Database

def create_cat(name: str) -> Cat:
    Database.create_cat(name)

def get_cat():
    return Database.get_cat()

def sleep():
    Database.sleep()

def wake_up():
    Database.wake_up()

def apply_action(action):
    cat = Database.get_cat()
    if action == 'Покормить' and cat.is_sleep:
        print('Спящего кота нельзя покормить.')
    elif action == 'Поиграть' and cat.is_sleep:
        cat.happiness = -5
        wake_up()
    elif action == 'Покормить':
        cat.satiety = 15
        cat.happiness = 5
        if cat.satiety > Cat.max_value:
            cat.happiness = -30
    elif action == 'Поиграть':
        cat.happiness = 15
        cat.satiety = -10
        if randint(1,3) == 1:
            cat.happiness = -cat.happiness
    elif action == 'Уложить спать':
        sleep()
    else:
        print('Что то не то')
    cat.set_image()


