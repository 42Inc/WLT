package main

import (
	"flag"
	"fmt"
	"math"
	"os"
)

var (
	Pexp      float64 = 0.0
	distance  float64 = 0.0
	frequency float64 = 0.0
	TxPAP     float64 = 0.0
	RxPUA     float64 = 0.0
	AgAP      float64 = 0.0
)

func initFlags() {
	flag.Usage = usage
	flag.Float64Var(&Pexp, "p", -53,
		"Experimental P (Pexp)")
	flag.Float64Var(&distance, "d", 2,
		"Distance")
	flag.Float64Var(&frequency, "f", 2462,
		"Frequency (MHz)")
	flag.Float64Var(&TxPAP, "tx", 16,
		"TxAP (dB)")
	flag.Float64Var(&AgAP, "ag", 2.5,
		"Antenna Gain (dB)")
	flag.Parse()
}

func usage() {
	fmt.Fprintf(os.Stderr, "Usage: %s [params]\n", os.Args[0])
	flag.PrintDefaults()
	os.Exit(1)
}

func getPL(f float64, d float64) float64 {
	var res float64 = 0.0
	res = 26*math.Log10(f) + 22.7 + 36.7*math.Log10(d)
	return res
}

func main() {
	initFlags()

	var (
		Alow   float64 = -10
		Aup    float64 = 10
		Amid   float64 = 0
		Blow   float64 = -100
		Bup    float64 = 100
		Bmid   float64 = 0
		RxPUA  float64 = 0.0
		PL     float64 = 0.0
		PLg     float64 = 0.0
		eps    float64 = 0.01
		scale  float64 = 0.5
		minMod float64 = math.MaxFloat64
		i      float64 = 0
		j      float64 = 0
	)

	PLg = getPL(frequency, distance)
	RxPUA = TxPAP + AgAP - PLg
	fmt.Printf("PL before optimization: [%f | %f]\n", PLg, scale)
	fmt.Printf("Receive Power UA: [%f | %f]\n", RxPUA, Pexp)
	fmt.Printf("=============================\n")

	for math.Abs(Pexp - RxPUA) > eps {
		scale = scale / 2
		minMod = math.MaxFloat64
		for i = 0; i < (Aup - Alow); i = i + scale {
			for j = 0; j < (Bup - Blow); j = j + scale {
				PL = (Alow+i)*PLg + (Blow + j)
				RxPUA = TxPAP + AgAP - PL
				if minMod >= math.Pow(Pexp - RxPUA, 2) && ((Alow+i) < 0 || (Alow+i) > 0) {
					minMod = math.Pow(Pexp - RxPUA, 2)
					Amid = (Alow + i)
					Bmid = (Blow + j)
				}
				// fmt.Printf("AB: [%f %f %f %f [%f %f] %f]\n", Amid, Bmid, i, j,math.Pow(Pexp - RxPUA, 2),minMod, RxPUA)
			}
		}
		PL = Amid*PLg + Bmid
		RxPUA = TxPAP + AgAP - PL
		fmt.Printf("PL optimization: [%f | %f]\n", PL, scale)
		fmt.Printf("Receive Power UA: [%f | %f]\n", RxPUA, Pexp)
		fmt.Printf("A: [%f %f %f]\n", Alow, Amid, Aup)
		fmt.Printf("B: [%f %f %f]\n", Blow, Bmid, Bup)
		fmt.Printf("=============================\n")
	}

	PL = Amid*PLg + Bmid
	RxPUA = TxPAP + AgAP - PL
	fmt.Printf("PL after optimization: [%f | %f]\n", PL, scale)
	fmt.Printf("Receive Power UA: [%f | %f]\n", RxPUA, Pexp)

	fmt.Printf("A: [%f %f %f]\n", Alow, Amid, Aup)
	fmt.Printf("B: [%f %f %f]\n", Blow, Bmid, Bup)
	fmt.Printf("eps: [%f]\n", eps)
}
