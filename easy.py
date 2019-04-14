# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._is_moving = False
        self._speed = 0
        self._is_police = False

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_name(self):
        return self._name

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def is_moving(self):
        return self._is_moving

    def is_police(self):
        return self._is_police

    def go(self):
        if not self._is_moving:
            print('{} начинает движение.'.format(self._name))
            self._is_moving = True

    def stop(self):
        if self._is_moving:
            print('{} останавливается.'.format(self._name))
            self._is_moving = False

    def turn(self, direction):

        if not self._is_moving:
            return
        if direction.lower() == 'b':
            print('{} разворачивается.'.format(self._name))
        if direction.lower() == 'l':
            print('{} поворачивает налево.'.format(self._name))
        if direction.lower() == 'r':
            print('{} поворачивает направо.'.format(self._name))


class TownCar(Car):

    def __init__(self, name, color, capacity):
        super().__init__(name, color)
        self._speed = 60
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity

    def set_is_police(self, is_police):
        self._is_police = bool(is_police)


class SportCar(Car):

    def __init__(self, name, color, engine_power):
        super().__init__(name, color)
        self._speed = 200
        self._engine_power = engine_power

    def get_engine_power(self):
        return self._engine_power

    def set_is_police(self, is_police):
        self._is_police = bool(is_police)


class WorkCar(Car):

    def __init__(self, name, color, load_capacity):
        super().__init__(name, color)
        self._speed = 40
        self._load_capacity = load_capacity

    def get_load_capacity(self):
        return self._load_capacity

    def load(self):
        print('{} грузится.'.format(self._name))

    def unload(self):
        print('{} разгружается.'.format(self._name))


class PoliceCar(Car):

    def __init__(self, name, color, police_station):
        super().__init__(name, color)
        self._is_police = True
        self._speed = 120
        self._police_station = police_station
        self._is_alarm = False

    def alarm_on(self):
        if not self._is_alarm:
            print('{} включает сирену.'.format(self._name))
            self._is_alarm = True

    def alarm_off(self):
        if self._is_alarm:
            print('{} выключает сирену.'.format(self._name))
            self._is_alarm = False

    def get_alarm(self):
        return self._is_alarm

    def get_police_station(self):
        return self._police_station


my_town_car = TownCar('Lincoln Town Car', 'чёрный', 6)
my_sport_car = SportCar('Nissan GT-R', 'красный', 600)
my_work_car = WorkCar('Liebherr T282B', 'жёлтый', 363)
my_police_car = PoliceCar('Ford Crown Victoria', 'белый', 'Ontario Police Department OR 97914')

print('Автомобиль :', my_police_car.get_name())
print('Является полицейским автомобилем :', my_police_car.is_police())
print('Цвет :', my_police_car.get_color())
print('Полицейский участок :', my_police_car.get_police_station())
print('Максимальная скорость :', my_police_car.get_speed())

my_police_car.go()
my_police_car.turn('r')
my_police_car.alarm_on()
print('Автомобиль движется :', my_police_car.is_moving())
print('Сирена работает :', my_police_car.get_alarm())
my_police_car.stop()
my_police_car.alarm_off()
print('Автомобиль движется :', my_police_car.is_moving())
print('Сирена работает :', my_police_car.get_alarm())
