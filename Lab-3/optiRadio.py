#!/usr/bin/env python3

#
# Author: 42Inc
#

A = [-10,10]
B = [-100,100]

dist = [1, 2, 3, 4, 5, 6]
TxAP = 16			# dBm
TxUser = 20			# dBm
channel = 6
FreqAP = 2.437		# GHz
RxSenseAP = 90		# dBm
expCount = 100
Pexp = []
Ptheo = []

def HalfLife3(inter):
	leftBorder = inter[0]
	rightBorder = inter[1]
	while (rightBorder - leftBorder > 1):
		length = rightBorder - leftBorder
		halflife = int(length / 2)
		mid = leftBorder + halflife
		if (leftBorder >= 0) and (mid < 0):
			rightBorder = mid
		else:
			leftBorder = mid
	return mid

def optiFunc(Amin, Bmin):
	L = [ 0.0 for cnt in range(len(dist))]
	for iter in range(len(dist)):
		PathLosses = 26 * np.log10(FreqAP) + 22.7 + 36.7 * np.log10(dist[iter])
		L[iter] = Amin * PathLosses + Bmin
		print("Distance =", dist[iter], "\tPathLosses =", PathLosses, "\tL =", L[iter])
	return L

def errorRate():
	for iter in range(expCount):
		err += (Ptheo - Pexp) ** 2
	return err

def main():
	Amin = HalfLife3(A)
	Bmin = HalfLife3(B)
	res = optiFunc(Amin, Bmin)
	# err = errorRate()

if __name__ == '__main__':
	try:
		import sys
		from time import sleep
		import numpy as np
		from math import pi
	except Exception as e:
		exit(e)
	main()
