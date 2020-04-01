#!/usr/bin/env python3

dataSize = 512											# Bits
SNR = 0													# dB

def genRnd():
	rndArr = [0 for cnt in range(dataSize)]
	for cnt in range(dataSize):
		rndArr[cnt] = rnd.randint(0,1)
	return rndArr

def QPSK(_inputData):
	flg = 0
	_dataQPSK = [0 for cnt in range(int(dataSize/2))]
	for cnt in range(0,512,2):
		if _inputData[cnt] == 0:
			if _inputData[cnt+1] == 0:
				_dataQPSK[flg] = 0
			else:
				_dataQPSK[flg] = 1
		else:
			if _inputData[cnt+1] == 0:
				_dataQPSK[flg] = 2
			else:
				_dataQPSK[flg] = 3
		flg += 1
	return _dataQPSK

def encodeOFDM(_dataQPSK):
	_dataOFDM = [0 for cnt in range(int(dataSize/2))]
	return _dataOFDM

def genNoise(_dataOFDM):
	sigma = math.sqrt(1 / (math.log2(4) * 2 * 10 ** (0.1 * SNR)))
	signalNoise = sigma * math.cos(2 * math.pi * rnd.randint(0,1) * cmath.sqrt(math.log10(rnd.randint(1,2)))) +\
				sigma * math.cos(2 * math.pi * rnd.randint(0,1) * cmath.sqrt(math.log10(rnd.randint(1,2))))
	print(signalNoise)

def decodeOFDM():
	pass

def hardDecode():
	pass

def BitErrorRate():
	pass

def drawGraph():
	pass

def main():
	inputData = genRnd()
	dataQPSK = QPSK(inputData)
	dataOFDM = encodeOFDM(dataQPSK)
	dataTx = genNoise(dataOFDM)
	decodeOFDM()
	hardDecode()
	BitErrorRate()
	drawGraph()

if __name__ == '__main__':
	try:
		import sys
		import math
		import cmath
		import numpy as np
		import random as rnd
		import matplotlib.pyplot as plt
	except Exception as err:
		print("Error while loading dependencies:", err)
		exit(-1)
	main()
