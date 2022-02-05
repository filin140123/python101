class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Car is moving..."

    def stop(self):
        return "Car has stopped."

    def turn(self, direction):
        return f"Car turned {direction}."

    def show_speed(self):
        return f"Current speed: {self.speed}"


class TownCar(Car):
    def show_speed(self):
        return f"Current speed: {self.speed}" if self.speed <= 60 else "Сar is exceeding the speed limit!"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f"Current speed: {self.speed}" if self.speed <= 40 else "Сar is exceeding the speed limit!"


class PoliceCar(Car):
    pass


# Инстанции
town = TownCar(70, "white", "honda civic", False)
sport = SportCar(180, "red", "lamborgini", False)
work = WorkCar(35, "grey", "chery", False)
police = PoliceCar(80, "black", "ford interceptor", True)
cars = [town, sport, work, police]

# Доступ к атрибутам и вызов методов
for c in cars:
    print(c.color, c.speed, c.name, c.is_police)
    print(c.go(), c.stop(), c.turn("right"), c.turn("left"), c.show_speed())
