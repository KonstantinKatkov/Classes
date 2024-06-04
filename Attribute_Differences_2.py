# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества
# созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию


class Buiding:
    total = 0

    def __init__(self):
        self.count = Buiding.total
        Buiding.total += 1
        print(f'Объект номер {self.total}')


for i in range(40):
    b = Buiding()

    print(b, type(b))
