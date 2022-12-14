from matplotlib import pyplot as pp  # type: ignore
import numpy as np

MODEL_G: float = 9.8
MODEL_DT: float = 0.1


class Body:
    def __init__(self, x: float, y: float, vx: float, vy: float) -> None:
        """
        Создаем класс Тела:
        x - x-координата
        y - y-координата
        vx - проекция скорости на Ox
        vy - проекция скорости на Oy
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.traj_x: list[float] = []
        self.traj_y: list[float] = []

    def advance(self) -> None:
        self.vy -= MODEL_G * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.x += self.vx * MODEL_DT
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)


class Rocket(Body):

    def __init__(self, x: float, y: float, vx: float, vy: float) -> None:
        """
        Создаем класс Ракеты:
        angle - наклон ракеты относительно Ох
        mass - масса
        fuel_cons - расход топлива
        fuel_v - скорость истекающих газов
        Данные для последних трех свойств взяты с ракеты Фау-2
        """
        super().__init__(x, y, vx, vy)
        self.angle: float = np.pi / 4
        self.mass: float = 12500
        self.fuel_cons: int = 127
        self.fuel_v: int = 2050

    def advance(self) -> None:
        super().advance()
        if self.mass < 4000:
            return
        self.vy += MODEL_DT * (self.fuel_cons * self.fuel_v * np.sin(self.angle)) / self.mass
        self.vx += MODEL_DT * (self.fuel_cons * self.fuel_v * np.cos(self.angle)) / self.mass
        self.mass -= self.fuel_cons * MODEL_DT


r: Rocket = Rocket(0, 0, 0, 0)
b: Body = Body(0, 0, 10, 10)

for bb in [r, b]:
    for i in np.arange(0, 2, MODEL_DT):
        bb.advance()
    pp.plot(bb.traj_x, bb.traj_y)


pp.show()
