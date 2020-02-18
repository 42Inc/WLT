#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

def radioCoverage(arg):
	drawgraph(x, y)

def drawGraph(x, y):
	plt.plot(x, y)
	plt.show()


TxAP = 20
TxUser = 20
AntG = 6
PenLoss = 12
IntMrg = 5
freqRng = [2.4, 5]
freqUL = 15
freqDL = 20
N_AP = 5
N_User = 8
SINR_UL = 15
SINR_DL = 17
dist = 1
bandWidth = 20
ThermalNoise = -174 + np.log10(bandWidth)
RxSensUser = ThermalNoise + N_User + SINR_DL
RxSensAP = ThermalNoise + N_AP + SINR_UL

PathLosses = 26 * np.log10(freqRng[0]) + 22.7 + 36.7 * np.log10(dist)

MAPL_UL = TxUser + AntG - PenLoss - IntMrg - PathLosses - RxSensUser
MAPL_DL = TxAP + AntG - PenLoss - IntMrg - PathLosses - RxSensAP
distUL = 10 ** ((MAPL_UL - (26 * np.log10(freqRng[0]) + 22.7)) / 36.7) 
distDL = 10 ** ((MAPL_DL - (26 * np.log10(freqRng[0]) + 22.7)) / 36.7) 
print(distUL)
print(distDL)
print(MAPL_UL)
print(MAPL_DL)

#radioCoverage()
#drawGraph()