#!/usr/bin/env python3

#
# Author: 42Inc
#

# Исходные данные для расчета абонентской емкости сетей 2G
transceiverPerBS = 3					# Число приемопередатчиков на одной БС
controlChannel = 2						# Число каналов управления на одной БС
Pblock = 0.05							# Вероятность отказа в установлении соединения абонента
loadIntensity = 0.03					# Интенсивность нагрузки одного абонента в ЧНН (Час Наибольшей Нагрузки): g

# Исходные данные для расчета абонентской емкости сетей 4G
# Режим MIMO: 2x2, пространственное мультиплексирование (spacial multiplexing);
# Используемая схема модуляции и кодирования MCS: QAM16 4/5;
# Режим дуплексирования UL и DL: FDD;
bandwith = 10							# Ширина полосы частот, МГц
cyclePrefix = 1							 # Циклический префикс ???
sendSpeed = 20000						# Требуемая скорость передачи данных для одного голосового абонента на физическом уровне: бит/с
resourceCost = 0.3						# Затраты частотно-временных ресурсов на каналы управления и вспомогательные сигналы: %
harq = 0.1								# Процент ретрансмиссий MAC-уровня HARQ: %

def factorial(num):
	factVal = 1
	i = 0
	if num < 0:
		return 0
	else:
		for i in range(1, int(num)):
			factVal *= i
	return factVal

def capacity2G():
	res = 0
	left = 0
	eps = 0.01
	right = transceiverPerBS
	while (abs(m.factorial(transceiverPerBS) * Pblock - res) > eps):
		mid = (right - left) / 2 + left
		res = mid ** 3 / m.e ** mid
		if res > m.factorial(transceiverPerBS) * Pblock:
			right = mid
		else:
			left = mid
	abonentsCnt = res / loadIntensity
	print("2G abonents total:", abonentsCnt)

def capacity4G():
	smblCnt = 7 * 50 * 2 * 1000 * 2
	actualData = smblCnt - smblCnt / 5 - smblCnt * harq - smblCnt * resourceCost
	transmissionSpeed = actualData * 3
	abonentsCnt = transmissionSpeed / sendSpeed
	print("4G abonents total:", abonentsCnt)

def main():
	capacity2G()
	capacity4G()

if __name__ == '__main__':
	try:
		import math as m
		import numpy as np
	except Exception as e:
		exit(e)
	main()
