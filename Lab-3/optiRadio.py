#!/usr/bin/env python3

#
# Author: 42Inc
#

A = [-10,10]
B = [-100,100]

dist = 2
TxAP = 17			# dBm
TxUser = 20			# dBm
channel = 6
FreqAP = 2.462		# GHz
RxSenseAP = 71		# dBm
expCount = 100
Pexp = -53
Ptheo = 0

def optiFunc(Ad, Bd):
	minO = 100000000
	minA = 0
	minB = 0
	# L = [ 0.0 for cnt in range(len(dist))]
	for iter1 in range(Ad[1] - Ad[0]):
		for iter2 in range(Bd[1] - Bd[0]):
			PathLosses = 26 * np.log10(FreqAP) + 22.7 + 36.7 * np.log10(dist)
			Ptheo = (iter1 + Ad[0]) * PathLosses + (iter2 + Bd[0])
			# print("Distance =", dist, "\tPathLosses =", Ptheo, "\tPexp =", Pexp, "\tminA =", (iter1 + Ad[0]), "\tminB =", (iter2 + Bd[0]) )
			if minO > (Ptheo - Pexp) ** 2 and (iter1 + Ad[0]) != 0:
				minO =  (Ptheo - Pexp) ** 2
				minA = (iter1 + Ad[0])
				minB = (iter2 + Bd[0])
	PathLosses = 26 * np.log10(FreqAP) + 22.7 + 36.7 * np.log10(dist)
	Ptheo = float(minA) * float(PathLosses) + minB
	print("Distance =", dist, "\tPathLosses =", Ptheo, "\tPexp =", Pexp, "\tminA =", minA, "\tminB =", minB)

def main():
	optiFunc(A, B)

if __name__ == '__main__':
	try:
		import sys
		from time import sleep
		import numpy as np
		from math import pi
	except Exception as e:
		exit(e)
	main()
