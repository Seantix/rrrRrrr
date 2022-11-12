from matplotlib import pyplot as pp
import numpy as np

MODEL_G = 9.8
MODEL_DT = 0.1
class Rocket:
    def __init__(self, x, y, vx, vy):
        """
        Создаем класс Ракеты:

        x - x-координата
        y - y-координата
        vx - проекция скорости на Ox
        vy - проекция скорости на Oy
        angle - наклон ракеты относительно Ох
        mass - масса
        fuel_cons - расход топлива
        fuel_v - скорость истекающих газов

        Данные для последних трех свойств взяты с ракеты Фау-2
        """
        self.x = x
        self.angle = np.pi / 4
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = 12500
        self.fuel_cons = 127
        self.fuel_v = 2050
        self.traj_x = []
        self.traj_y = []

    def advance(self):
        """
        Метод для "ракетного полета". Проекции скоростей меняются согласно уравнению Мещерского, масса уменьшается очевидным образом.
        """
        self.vy += MODEL_DT * (self.mass * MODEL_G + self.fuel_cons * self.fuel_v * np.sin(self.angle)) / self.mass
        self.vx += MODEL_DT * (self.fuel_cons * self.fuel_v * np.cos(self.angle)) / self.mass
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.mass -= self.fuel_cons * MODEL_DT
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)
    
    def free(self):
        """
        Метод для "свободного" полета и падения, т.е. когда топливо кончилось.
        """
        self.vy -= MODEL_G * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.x += self.vx * MODEL_DT
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)

r = Rocket(0, 0, 0, 0)

for i in np.arange (0, 200, MODEL_DT):
    while r.y >= 0:
        if r.mass > 4000:
            r.advance()
        else:
            r.free()


pp.plot(r.traj_x, r.traj_y)
pp.show()