#!/usr/bin/env python3

#
# Author: 42Inc
#


dist = 1 				# Kilometer
freqTrans = 900 		# MHz
heightBS = 17			# Meter
heightMS = 1.5 			# Meter

def hataUrban():
	antCorrFact_Wiki = 3.2 * ((np.log10(11.75 * heightMS)) ** 2) - 4.97
	antCorrFact_Lect = 3.2 * (np.log10(11.75 * heightMS)) - 4.97

	# Wiki's formula
	hataU_Wiki = 69.55 + 26.66 * np.log10(freqTrans) - 13.82 * np.log10(heightBS) -\
				antCorrFact_Wiki + (44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist)
	# Lection's formula
	hataU_Lect = 69.55 + 26.66 * np.log10(freqTrans) - 13.82 * np.log10(heightBS) -\
	 			antCorrFact_Lect + (44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist)
	return hataU_Wiki, hataU_Lect

def hataSub():
	antCorrFact_Wiki = 0.8 + (1.1 * np.log10(freqTrans) - 0.7) * heightMS - 1.56 * np.log10(freqTrans)
	antCorrFact_Lect = 3.2 * (np.log10(11.75 * heightMS)) - 4.97

	# Wiki's formula
	hataS_Wiki = 69.55 + 26.66 * np.log10(freqTrans) - 13.82 * np.log10(heightBS) -\
				antCorrFact_Wiki + (44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) -\
				2 * ((np.log10(freqTrans / 28)) ** 2) - 5.4
	# Lection's formula
	hataS_Lect = 69.55 + 26.66 * np.log10(freqTrans) - 13.82 * np.log10(heightBS) -\
	 			antCorrFact_Lect + (44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) -\
				2 * ((np.log10(freqTrans / 28)) ** 2) - 5.4
	return hataS_Wiki, hataS_Lect

def hataOpen():
	antCorrFact_Wiki = 0.8 + (1.1 * np.log10(freqTrans) - 0.7) * heightMS - 1.56 * np.log10(freqTrans)
	antCorrFact_Lect = 0.8 + (1.1 * np.log10(freqTrans) - 0.7) * heightMS - 1.56 * np.log10(freqTrans)

	# Wiki's formula
	hataO_Wiki = 69.55 + 26.66 * np.log10(freqTrans) - 13.82 * np.log10(heightBS) -\
				antCorrFact_Wiki + (44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) -\
				4.78 * (np.log10(freqTrans) ** 2) + 18.33 * (np.log10(freqTrans)) - 40.94
	# Lection's formula
	hataO_Lect = 69.55 + 26.66 * np.log10(freqTrans) - 13.82 * np.log10(heightBS) -\
	 			antCorrFact_Lect + (44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) -\
				4.78 * (np.log10(freqTrans) ** 2) - 18.33 * (np.log10(freqTrans)) + 40.94
	return hataO_Wiki, hataO_Lect

def costUrban():
	# Wiki's formula
	costU_Wiki = 46.3 + 33.9 * (np.log10(freqTrans)) - 13.82 * (np.log10(heightBS)) -\
				(3.2 * (np.log10(11.75 * heightMS)) ** 2 - 4.97) +\
				(44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) + 3
	# Lection's formula
	costU_Lect = 46.3 + 33.9 * (np.log10(freqTrans)) - 13.82 * (np.log10(heightBS)) -\
				((1.1 * np.log10(freqTrans) - 0.7) * heightMS - (1.5 * np.log10(freqTrans) - 0.8)) - 3 +\
				(44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) + 3
	return costU_Wiki, costU_Lect

def costSub():
	# Wiki's formula
	costS_Wiki = 46.3 + 33.9 * (np.log10(freqTrans)) - 13.82 * (np.log10(heightBS)) -\
				((1.1 * np.log10(freqTrans) - 0.7) * heightMS - (1.56 * np.log10(freqTrans) - 0.8)) +\
				(44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist)
	# Lection's formula
	costS_Lect = 46.3 + 33.9 * (np.log10(freqTrans)) - 13.82 * (np.log10(heightBS)) -\
	 			((1.1 * np.log10(freqTrans) - 0.7) * heightMS - (1.5 * np.log10(freqTrans) - 0.8)) -\
				(2 * ((np.log10(freqTrans / 28)) ** 2) + 5.4) +\
				(44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) + 3
	return costS_Wiki, costS_Lect

def costOpen():
	# Wiki's formula
	costO_Wiki = 46.3 + 33.9 * (np.log10(freqTrans)) - 13.82 * (np.log10(heightBS)) -\
				((1.1 * np.log10(freqTrans) - 0.7) * heightMS - (1.56 * np.log10(freqTrans) - 0.8)) +\
				(44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist)
	# Lection's formula
	costO_Lect = 46.3 + 33.9 * (np.log10(freqTrans)) - 13.82 * (np.log10(heightBS)) -\
	 			((1.1 * np.log10(freqTrans) - 0.7) * heightMS - (1.5 * np.log10(freqTrans) - 0.8)) -\
				(4.78 * (np.log10(freqTrans) ** 2) - 18.33 * (np.log10(freqTrans)) + 40.94) +\
				(44.9 - 6.55 * np.log10(heightBS)) * np.log10(dist) + 3
	return costO_Wiki, costO_Lect

def drawTable():
	print()

def main():
	hataU_Wiki, hataU_Lect = hataUrban()	# dB
	hataS_Wiki, hataS_Lect = hataSub()		# dB
	hataO_Wiki, hataO_Lect = hataOpen()		# dB

	costU_Wiki, costU_Lect = costUrban()	# dB
	costS_Wiki, costS_Lect = costSub()		# dB
	costO_Wiki, costO_Lect = costOpen()		# dB

	print("Path Losses: Okumura Hata in Urban Env")
	print("Wiki:", hataU_Wiki, "\tLection:", hataU_Lect,"\n")
	print("Path Losses: Okumura Hata in Suburban Env")
	print("Wiki:", hataS_Wiki, "\tLection:", hataS_Lect,"\n")
	print("Path Losses: Okumura Hata in Open Env")
	print("Wiki:", hataO_Wiki, "\tLection:", hataO_Lect,"\n")

	print("Path Losses: COST Hata in Urban Env")
	print("Wiki:", costU_Wiki, "\tLection:", costU_Lect,"\n")
	print("Path Losses: COST Hata in Suburban Env")
	print("Wiki:", costS_Wiki, "\tLection:", costS_Lect,"\n")
	print("Path Losses: COST Hata in Open Env")
	print("Wiki:", costO_Wiki, "\tLection:", costO_Lect,"\n")

	drawTable()

if __name__ == "__main__":
	try:
		import sys
		import numpy as np
		import texttable as tt
	except Exception as err:
		print(f"Error while loading dependencies:", err)
		exit(-1)
	main()
