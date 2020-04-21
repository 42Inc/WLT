#!/usr/bin/env python3

#
# Author: 42Inc
#

A = [-10,10]
B = [-100,100]

TxAP = 16			# dBm
TxUser =			# dBm
channel = 6
FreqAP = 2437		# MHz
RxSenseAP = 90		# dBm

Pexp = []
Ptheo = []

def optiFunc():
	X(d) = 	26 * np.log10(FreqAP) + 22.7 + 36.7 * np.log10(d)
	L(d) = A * X(d) + B

def errorRate():
	for iter in range(expCount):
		err += (Ptheo - Pexp) ** 2
	return err

def main():
	res = optiFunc()
	err = errorRate()

if __name__ == '__main__':
	try:
		import sys
		import numpy as np
		from math import pi
	except Exception as e:
		exit(e)
	main()
