#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#импорт нужных библиотек
import math
import numpy
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':                        #условие
    arguments = numpy.arange(100, 200, 1)       #arguments - множество значений в интервале от 0 до 200 с шагом 0,1
    mpp.plot(                                   #функция посторения графика
        arguments,                             
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  #перебираем значения из arguments и считаем значение функции в них
    )
    mpp.show()                                  #показать график