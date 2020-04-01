#!/usr/bin/env python3

def main():
	pass

if __name__ == '__main__':
	try:
		import sys
		import numpy as np
		import math
		from texttable import Texttable as TT
	except Exception as err:
		print("Error while loading dependencies:", err)
		exit(-1)
	main()
