from random import randint



class Cat:
    min_value = 0
    max_value = 100

    def __init__(self, name: str):
        self.name = name
        self._age = randint(1, 5)
        self._satiety = randint(Cat.min_value + 20, Cat.max_value)
        self._happiness = randint(Cat.min_value + 20, Cat.max_value)
        self.is_sleep = False
        self.image = None
        self.set_image()
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value:int):
        self._age = value
    
    @property
    def satiety(self):
        return self._satiety
    
    @satiety.setter
    def satiety(self, value:int):
        self._satiety += value

    @property
    def happiness(self):
        return self._happiness
    
    @happiness.setter
    def happiness(self, value:int):
        self._happiness += value
    
    def set_image(self):
        if self._happiness < 50:
            self.image = 'catapp/images/cat_sad.jpg'
        else:
            self.image = 'catapp/images/cat_happy.jpg'
    
    



class Database:
    cat = None

    @staticmethod
    def create_cat(name):
        Database.cat = Cat(name)
    
    @staticmethod
    def set_satiety(value):
        Database.cat.satiety += value
    
    @staticmethod
    def set_happiness(value):
        Database.cat.happiness += value
        
    @staticmethod
    def get_cat():
        return Database.cat
    
    @staticmethod
    def sleep():
        Database.cat.is_sleep = True
    
    @staticmethod
    def wake_up():
        Database.cat.is_sleep = False
