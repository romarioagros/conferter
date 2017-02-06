#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import osa
import math


def fahrenheit(file):
    temp_list = []
    f = open(file_temp, 'r', encoding='utf-8')
    for line in f:
        temp_list.append(int(" ".join(line.split('F'))))
    # print (sum(temp_list)/len(temp_list))
    average_f = sum(temp_list) / len(temp_list)
    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.Client(URL)
    responce = client.service.ConvertTemp(Temperature=average_f, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
    return int(round(responce, 0))


def curensy_to_rub(file):
    curensy_list = []
    f = open(file_curensy)
    for line in f:
        curensy_list.append(line.split())

    URL_money = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client = osa.Client(URL_money)
    amount_of_ruble = []

    for item in curensy_list:
        amount = (float(item[1]))
        Currency = item[2]
        responce = client. service.ConvertToNum(amount=amount, fromCurrency=Currency, toCurrency='rub', rounding='TRUE')
        amount_of_ruble.append(math.ceil(int(responce)))

    return sum(amount_of_ruble)


def miles_to_km(file):


    curensy_list=[]
    f = open(file_curensy)
    for line in f:
        curensy_list.append(line.split())

    lenght = float(''.join(curensy_list[0][1].split(',')))
    URL_money = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.Client(URL_money)
    summ_of_lenght = []
    for item in curensy_list:
        lenght = float(''.join(item[1].split(',')))
        responce = client.service.ChangeLengthUnit(LengthValue=lenght, fromLengthUnit='Miles',
                                                   rounding='TRUE', toLengthUnit='Kilometers')
        summ_of_lenght.append(responce)
    return round(sum(summ_of_lenght) ,  2)


# Пути файлов принимаемые для функций
file_temp = r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-4\Homework\temps.txt'
file_curensy = r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-4\Homework\currencies.txt'
file_travel = r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-4\Homework\travel.txt'

# вызов функций и печать
print('средняя температура недели ', fahrenheit(file_temp), 'C')
print("общая сумма необходимая для кругосветного путешествия -" , curensy_to_rub(file_travel) , "руб")
print('суммарное расстояние пути ', miles_to_km(file_travel) , 'километров')
