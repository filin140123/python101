from time import sleep


class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 4}

    def running(self):
        for c, t in self.__color.items():
            print(f"{c.title()} light running for {t} seconds...")
            sleep(t)


trl = TrafficLight()
trl.running()

# Допускаю, что неверно понял условия задания, буду рад обратной связи на этот счет
