#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def drawGraph(y1, y2, z1, z2, x):
	plt.plot(x, y1, label='PathLosses 2.4 GHz')
	plt.plot(x, y2, label='PathLosses 5 GHz')
	plt.plot(x, z2[0], label='MAPL_UL')
	plt.plot(x, z2[1], label='MAPL_DL')
	plt.ylabel('PL')
	plt.xlabel('Distance')
	plt.legend()
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
dist_array = [1, 2, 5, 10, 15, 20, 30, 40, 50, 100]
bandWidth = [20, 15]
ThermalNoise = [0,0]
ThermalNoise[0] = -174 + 10 * np.log10(bandWidth[0] * 1000000)
ThermalNoise[1] = -174 + 10 * np.log10(bandWidth[1] * 1000000)
RxSensUser = ThermalNoise[0] + N_User + SINR_DL
RxSensAP = ThermalNoise[1] + N_AP + SINR_UL

PathLosses_24 = np.zeros(10)
PathLosses_5 = np.zeros(10)
MAPL_array_24 = np.zeros((2, 10))
MAPL_array_5 = np.zeros((2, 10))
radioCoverage_24 = np.zeros((2, 1))
radioCoverage_5 = np.zeros((2, 1))

for cnt in range(10):
	PathLosses_24[cnt] = 26 * np.log10(freqRng[0]) + 22.7 + 36.7 * np.log10(dist_array[cnt])
	PathLosses_5[cnt] = 26 * np.log10(freqRng[1]) + 22.7 + 36.7 * np.log10(dist_array[cnt])

	MAPL_array_24[0, cnt] = TxUser + AntG - PenLoss - IntMrg - RxSensAP
	MAPL_array_24[1, cnt] = TxAP + AntG - PenLoss - IntMrg - RxSensUser
	MAPL_array_5[0, cnt] = TxUser + AntG - PenLoss - IntMrg - RxSensAP
	MAPL_array_5[1, cnt] = TxAP + AntG - PenLoss - IntMrg - RxSensUser

radioCoverage_24[0, 0] = 10 ** ((MAPL_array_24[0, 0] - (26 * np.log10(freqRng[0]) + 22.7)) / 36.7)
radioCoverage_5[0, 0] = 10 ** ((MAPL_array_5[0, 0] - (26 * np.log10(freqRng[1]) + 22.7)) / 36.7)

print("2.4 GHz - ", radioCoverage_24[0, 0],
	  "\n5 GHz - ", radioCoverage_5[0, 0])

drawGraph(PathLosses_24, PathLosses_5, MAPL_array_24, MAPL_array_5, dist_array)
