class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        Horse.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        Eagle.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)


    def get_pos(self):
        return (super().x_distance, super().y_distance)

    def voice(self):
        return print(super().sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()          # Pegasus НЕ издаёт звук "I train, eat, sleep, and repeat",
                    # т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.
