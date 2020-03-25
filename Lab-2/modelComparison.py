#!/usr/bin/env python3

# Author: 42Inc

global __hataU__
global __hataS__
global __hataO__

global __costU__
global __costS__
global __costO__

def hataUrban():
	print("Okay")

def hataSub():
	print("Okay")

def hataOpen():
	print("Okay")

def costUrban():
	print("Okay")

def costSub():
	print("Okay")

def costOpen():
	print("Okay")

def drawTable():
	print("Okay")

def main():
	hataUrban()
	hataSub()
	hataOpen()

	costUrban()
	costSub()
	costOpen()

	drawTable()

if __name__ == "__main__":
	try:
		import sys
		import numpy
		import texttable
	except Exception as err:
		print(f"Error while loading dependencies:", err)
		exit(-1)
	sys.exit(main())
