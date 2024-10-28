from threading import Thread
from time import sleep

total_enemies = 100


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global total_enemies
        days = 0
        print(f"{self.name}, на нас напали!")

        while total_enemies > 0:
            days += 1
            total_enemies -= self.power

            if total_enemies < 0:
                total_enemies = 0

            print(f"{self.name} сражается {days} день(дня)..., осталось {total_enemies} воинов.")

            sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
