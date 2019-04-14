# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Factory:
    def __init__(self, factory_name):
        self.factory_name = factory_name

    def purchase(self, name, type, color):
        self.new_toy = Toy(self.factory_name, name, type, color)
        self.new_toy.toy_type = "Животное" if type == 0 else "Персонаж мультфильма"
        print("Закупка сырья для игрушки: \"{}\" тип: \"{}\" цвет: \"{}\"".format(self.new_toy.toy_name,
                                                                                  self.new_toy.toy_type,
                                                                                  self.new_toy.toy_color))

    def sewing(self):
        print("Пошив игрушки ...")

    def paint(self):
        print("Окраска игрушки ...")

    def ready_toy(self):
        print("Игрушка готова: название: \"{}\", тип: \"{}\", цвет: \"{}\"".format(self.new_toy.toy_name,
                                                                                   self.new_toy.toy_type,
                                                                                   self.new_toy.toy_color))


class Toy(Factory):
    def __init__(self, factory_name, toy_name, toy_type, toy_color):
        Factory.__init__(self, factory_name)
        self.toy_name = toy_name
        self.toy_type = toy_type
        self.toy_color = toy_color


factory_star = Factory("ООО Звезда")
print(factory_star.purchase("Хрюша", 1, "розовый"))
print(factory_star.sewing())
print(factory_star.paint())
print(factory_star.ready_toy())


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Factory:
    def __init__(self, factory_name):
        self.factory_name = factory_name

    def purchase(self, name, type, color):
        self.new_toy = Toy(self.factory_name, name, color)
        # self.new_toy.toy_type = "Животное" if type == 0 else "Персонаж мультфильма"
        if type == 0:
            self.type_animals = Toy_type_animal(self.factory_name, name, color, type)
            self.type = "Животное"
        else:
            self.type_cartoon = Toy_type_cartoon(self.factory_name, name, color, type)
            self.type = "Персонаж мультфильма"
        print("Закупка сырья для игрушки: \"{}\" тип: \"{}\" цвет: \"{}\"".format(self.new_toy.toy_name, type,
                                                                                  self.new_toy.toy_color))

    def sewing(self):
        print("Пошив игрушки ...")

    def paint(self):
        print("Окраска игрушки ...")

    def ready_toy(self):
        print("Игрушка готова: название: \"{}\", тип: \"{}\", цвет: \"{}\"".format(self.new_toy.toy_name, self.type,
                                                                                   self.new_toy.toy_color))


class Toy(Factory):
    def __init__(self, factory_name, toy_name, toy_color):
        Factory.__init__(self, factory_name)
        self.toy_name = toy_name
        self.toy_color = toy_color


class Toy_type_animal(Toy):
    def __init__(self, factory_name, toy_name, toy_color, toy_type):
        super().__init__(factory_name, toy_name, toy_color)
        self.toy_type = toy_type


class Toy_type_cartoon(Toy):
    def __init__(self, factory_name, toy_name, toy_color, toy_type):
        super().__init__(factory_name, toy_name, toy_color)
        self.toy_type = toy_type


factory_star = Factory("ООО Звезда")
print(factory_star.purchase("Хрюша", 1, "розовый"))
print(factory_star.sewing())
print(factory_star.paint())
print(factory_star.ready_toy())
