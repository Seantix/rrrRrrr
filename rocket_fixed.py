from matplotlib import pyplot as pp
import numpy as np

MODEL_G = 9.8
MODEL_DT = 1



def RocketFlight(mass, angle, fuel_cons, fuel_v, fuel_vol, time):
    class Body:
        def __init__(self, x, y, vx, vy):
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
            self.traj_x = []
            self.traj_y = []
    
        def advance(self):
            self.vy -= MODEL_G * MODEL_DT
            self.y += self.vy * MODEL_DT
            self.x += self.vx * MODEL_DT
            self.traj_x.append(self.x)
            self.traj_y.append(self.y)


    class Rocket(Body):

        def __init__(self, x, y, vx, vy):
            """
            Создаем класс Ракеты:

            angle - наклон ракеты относительно Ох
            mass - масса
            fuel_cons - расход топлива
            fuel_v - скорость истекающих газов

            Данные для последних трех свойств взяты с ракеты Фау-2
            """
            super().__init__(x, y, vx, vy)
            self.angle = angle
            self.mass = mass
            self.fuel_cons = fuel_cons
            self.fuel_v = fuel_v       

        def advance(self):
            super().advance()
            if self.mass < mass - fuel_vol:
                return
            self.vy += MODEL_DT * (self.fuel_cons * self.fuel_v * np.sin(self.angle)) / self.mass
            self.vx += MODEL_DT * (self.fuel_cons * self.fuel_v * np.cos(self.angle)) / self.mass
            self.mass -= self.fuel_cons * MODEL_DT


    r = Rocket(0, 0, 0, 0)

    for i in np.arange (0, time, MODEL_DT):
        r.advance()

    return([r.traj_x[-1], r.traj_y[-1], r.vx, r.vy])


