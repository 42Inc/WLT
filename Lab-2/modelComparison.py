#!/usr/bin/env python3

#
# Author: 42Inc
#

dist = 1 									# Km
freqTrans = 900 							# MHz
ThermalNoise = -120.989 					# dB
heightBS = 17								# Meter
heightMS = 1.5 								# Meter
N_AP = 2									# dB
N_User = 7									# dB
SIN = 7										# dB
BPer = [22,17,12]							# dB
SlowFading = 13								# dB
FreqHop = 3									# dB
meter = 2									# dB
feeder = 3									# dB
BodyLoss = 3								# dB
TxPower_AP = 43								# dBm
TxPower_User = 30							# dBm
AntG = 17									# dBi
RxSenseUser = N_User + ThermalNoise + SIN	# dBm
RxSenseAP = N_AP + ThermalNoise + SIN		# dBm

def radiusHataUrban(hataU_Wiki):
	antCorrFact_Wiki = 3.2 * ((np.log10(11.75 * heightMS)) ** 2) - 4.97
	antCorrFact_Lect = 3.2 * (np.log10(11.75 * heightMS)) - 4.97

	# Wiki's formula
	radiusWiki = 10 ** ((hataU_Wiki - 69.55 - 26.66 * np.log10(freqTrans) + 13.82 * np.log10(heightBS) +\
				antCorrFact_Wiki) / (44.9 - 6.55 * np.log10(heightBS)))
	# Lection's formula
	radiusLect = 10 ** ((hataU_Wiki - 69.55 - 26.66 * np.log10(freqTrans) + 13.82 * np.log10(heightBS) +\
	 			antCorrFact_Lect) / (44.9 - 6.55 * np.log10(heightBS)))
	return radiusWiki, radiusLect

def radiusHataSub(hataS_Wiki):
	antCorrFact_Wiki = 0.8 + (1.1 * np.log10(freqTrans) - 0.7) * heightMS - 1.56 * np.log10(freqTrans)
	antCorrFact_Lect = 3.2 * (np.log10(11.75 * heightMS)) - 4.97

	# Wiki's formula
	radiusWiki = 10 ** ((hataS_Wiki - 69.55 - 26.66 * np.log10(freqTrans) + 13.82 * np.log10(heightBS) +\
				antCorrFact_Wiki + 2 * ((np.log10(freqTrans / 28)) ** 2) + 5.4) / (44.9 - 6.55 * np.log10(heightBS)))
	# Lection's formula
	radiusLect = 10 ** ((hataS_Wiki - 69.55 - 26.66 * np.log10(freqTrans) + 13.82 * np.log10(heightBS) +\
	 			antCorrFact_Lect + 2 * ((np.log10(freqTrans / 28)) ** 2) + 5.4) / (44.9 - 6.55 * np.log10(heightBS)))
	return radiusWiki, radiusLect

def radiusHataOpen(hataO_Wiki):
	antCorrFact_Wiki = 0.8 + (1.1 * np.log10(freqTrans) - 0.7) * heightMS - 1.56 * np.log10(freqTrans)
	antCorrFact_Lect = 0.8 + (1.1 * np.log10(freqTrans) - 0.7) * heightMS - 1.56 * np.log10(freqTrans)

	# Wiki's formula
	radiusWiki = 10 ** ((hataO_Wiki - 69.55 - 26.66 * np.log10(freqTrans) + 13.82 * np.log10(heightBS) +\
				antCorrFact_Wiki + 4.78 * (np.log10(freqTrans) ** 2) -\
				18.33 * (np.log10(freqTrans)) + 40.94) / (44.9 - 6.55 * np.log10(heightBS)))
	# Lection's formula
	radiusLect = 10 ** ((hataO_Wiki - 69.55 - 26.66 * np.log10(freqTrans) + 13.82 * np.log10(heightBS) +\
		 		antCorrFact_Lect + 4.78 * (np.log10(freqTrans) ** 2) +\
				18.33 * (np.log10(freqTrans)) - 40.94) / (44.9 - 6.55 * np.log10(heightBS)))

	return radiusWiki, radiusLect

def radiusCostUrban(costU_Wiki):
	# Wiki's formula
	radiusWiki = 10 ** ((costU_Wiki - 46.3 - 33.9 * (np.log10(freqTrans)) + 13.82 * (np.log10(heightBS)) +\
				(3.2 * (np.log10(11.75 * heightMS)) ** 2 - 4.97)  - 3) / (44.9 - 6.55 * np.log10(heightBS)))
	# Lection's formula
	radiusLect = 10 ** ((costU_Wiki - 46.3 - 33.9 * (np.log10(freqTrans)) + 13.82 * (np.log10(heightBS)) +\
				((1.1 * np.log10(freqTrans) - 0.7) * heightMS + (1.5 * np.log10(freqTrans) - 0.8))) /\
				(44.9 - 6.55 * np.log10(heightBS)) )
	return radiusWiki, radiusLect

def radiusCostSub(costS_Wiki):
	# Wiki's formula
	radiusWiki = 10 ** ((costS_Wiki - 46.3 - 33.9 * (np.log10(freqTrans)) + 13.82 * (np.log10(heightBS)) +\
				((1.1 * np.log10(freqTrans) - 0.7) * heightMS + (1.56 * np.log10(freqTrans) - 0.8))) /\
				(44.9 - 6.55 * np.log10(heightBS)))
	# Lection's formula
	radiusLect = 10 ** ((costS_Wiki - 46.3 - 33.9 * (np.log10(freqTrans)) + 13.82 * (np.log10(heightBS)) +\
	 			((1.1 * np.log10(freqTrans) - 0.7) * heightMS + (1.5 * np.log10(freqTrans) - 0.8)) +\
				(2 * ((np.log10(freqTrans / 28)) ** 2) + 5.4) + 3) / (44.9 - 6.55 * np.log10(heightBS)))
	return radiusWiki, radiusLect

def radiusCostOpen(costO_Wiki):
	# Wiki's formula
	radiusWiki = 10 ** ((costO_Wiki - 46.3 - 33.9 * (np.log10(freqTrans)) + 13.82 * (np.log10(heightBS)) +\
				((1.1 * np.log10(freqTrans) - 0.7) * heightMS + (1.56 * np.log10(freqTrans) - 0.8))) /\
				(44.9 - 6.55 * np.log10(heightBS)))
	# Lection's formula
	radiusLect = 10 ** ((costO_Wiki - 46.3 - 33.9 * (np.log10(freqTrans)) + 13.82 * (np.log10(heightBS)) +\
	 			((1.1 * np.log10(freqTrans) - 0.7) * heightMS + (1.5 * np.log10(freqTrans) - 0.8)) +\
				(4.78 * (np.log10(freqTrans) ** 2) - 18.33 * (np.log10(freqTrans)) + 40.94)  - 3) /\
				(44.9 - 6.55 * np.log10(heightBS)))
	return radiusWiki, radiusLect

def radioCoverage2G(radiusArr):
	radioCoverageArr = [ 0.0 for cnt in range(12)]
	for cnt in range(12):
		radioCoverageArr[cnt] = (radiusArr[cnt] ** 2 - (heightBS / 1000) ** 2) * pi
	return radioCoverageArr

def drawTable(radius, coverage):
	comparisonTable = TT()
	comparisonTable.set_cols_width([15,10,10,10,10,10,10,10,10])
	comparisonTable.set_cols_align(["c"] * 9)
	comparisonTable.header(['','Okumura Hata','','','','COST Hata','','',''])
	comparisonTable.add_row(['','Radius','','Area','','Radius','','Area',''])
	comparisonTable.add_row(['','Wiki','Lection','Wiki','Lection','Wiki','Lection','Wiki','Lection'])
	comparisonTable.add_row(['Urban Env',str(radius[0]),str(radius[1]),str(coverage[0]),str(coverage[1]),str(radius[6]),str(radius[7]),str(coverage[6]),str(coverage[7])])
	comparisonTable.add_row(['Suburban Env',str(radius[2]),str(radius[3]),str(coverage[2]),str(coverage[3]),str(radius[8]),str(radius[9]),str(coverage[8]),str(coverage[9])])
	comparisonTable.add_row(['Open Env',str(radius[4]),str(radius[5]),str(coverage[4]),str(coverage[5]),str(radius[10]),str(radius[11]),str(coverage[10]),str(coverage[11])])
	print(comparisonTable.draw())

def main():
	# Counting MAPL Uplink and Downlink
	MAPL_DL_Urban = TxPower_AP + AntG - feeder - RxSenseUser - SlowFading - FreqHop - BodyLoss - BPer[0]
	MAPL_UL_Urban = TxPower_User + AntG - feeder - RxSenseAP - SlowFading - FreqHop - BodyLoss - BPer[0]
	MAPL_DL_SubUrban = TxPower_AP + AntG - feeder - RxSenseUser - SlowFading - FreqHop - BodyLoss - BPer[1]
	MAPL_UL_SubUrban = TxPower_User + AntG - feeder - RxSenseAP - SlowFading - FreqHop - BodyLoss - BPer[1]
	MAPL_DL_Open = TxPower_AP + AntG - feeder - RxSenseUser - SlowFading - FreqHop - BodyLoss - BPer[2]
	MAPL_UL_Open = TxPower_User + AntG - feeder - RxSenseAP - SlowFading - FreqHop - BodyLoss - BPer[2]

	# Counting radiuses of MAPL distances
	radiusArr = [ 0.0 for cnt in range(12)]
	radiusArr[0], radiusArr[1] = radiusHataUrban(MAPL_UL_Urban)			# Km
	radiusArr[2], radiusArr[3] = radiusHataSub(MAPL_UL_SubUrban)		# Km
	radiusArr[4], radiusArr[5] = radiusHataOpen(MAPL_UL_Open)			# Km
	radiusArr[6], radiusArr[7] = radiusCostUrban(MAPL_UL_Urban)			# Km
	radiusArr[8], radiusArr[9] = radiusCostSub(MAPL_UL_SubUrban)		# Km
	radiusArr[10], radiusArr[11] = radiusCostOpen(MAPL_UL_Open)			# Km

	# Counting radio coverage for 2G networks with both formulas
	radioCoverageArr = [ 0.0 for cnt in range(12)]
	radioCoverageArr = radioCoverage2G(radiusArr)						# Km^2

	drawTable(radiusArr, radioCoverageArr)

if __name__ == "__main__":
	try:
		import sys
		import numpy as np
		from math import pi
		from texttable import Texttable as TT
	except Exception as err:
		print("Error while loading dependencies:", err)
		exit(-1)
	main()
