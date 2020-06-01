package main

import (
	"fmt"
	"math"
	"os"
	"os/exec"
	"runtime"

	"./CourseConfig"
)

var radius_is_print bool = false
var spectr_is_print bool = false

func main() {
	var (
		conf              CourseConfig.Config = CourseConfig.Test
		distance          float64             = 1E+5
		InteferenceMargin float64             = 5
		MaxDistance       float64             = 0.0
		Radius            float64             = 0.0
		SqNodeBase        float64             = 0.0
		SpeedRequired     float64             = 0.0
		TxPowerUserAgent  float64             = 24
	)
	clrscr()
	CourseConfig.PrintJsonConfig(conf)
	PathLoses := getPathLoses(conf, distance)
	RequireSINRBS, RequireSINRUA := getRequireSINR(conf)
	ThermalNoise := getThermalNoise(conf)
	RxSenseBS, RxSenseUE := getRxSense(conf)
	TxPowerNodeBase := 10 * math.Log10(conf.TxPowerNodeBase*1E+3)
	MAPLDL := conf.AntennaGainNodeBase + TxPowerNodeBase - RxSenseUE -
		conf.FeederLoses - InteferenceMargin - conf.PenetrationLoss
	MAPLUL := conf.AntennaGainNodeBase + TxPowerUserAgent - RxSenseBS -
		conf.FeederLoses - InteferenceMargin - conf.PenetrationLoss

	if MAPLDL < MAPLUL {
		MaxDistance = binSearchDistanceByPL(0, 1E+4, MAPLDL, conf)
	} else {
		MaxDistance = binSearchDistanceByPL(0, 1E+4, MAPLUL, conf)
	}
	Radius = math.Sqrt(math.Pow(MaxDistance, 2) - math.Pow((conf.HeightNodeBase-conf.HeightUserAgent), 2))
	SqNodeBase = math.Pi * math.Pow(Radius, 2)
	SpeedRequired = conf.AbonentsCount * conf.MaxDL * 8 / 3600
	fmt.Printf("RequireSINRBS: %f dB\n", RequireSINRBS)
	fmt.Printf("RequireSINRUA: %f dB\n", RequireSINRUA)
	fmt.Printf("ThermalNoise: %f\n", ThermalNoise)
	fmt.Printf("MAPL_DL : %.2f dB\n", MAPLDL)
	fmt.Printf("MAPL_UL : %.2f dB\n", MAPLUL)
	fmt.Printf("Max distance : %.2f m\n", MaxDistance)
	fmt.Printf("PathLoses for %.2f m: %f dB\n", distance, PathLoses)
	fmt.Printf("RxSense BS: %.2f dB\n", RxSenseBS)
	fmt.Printf("RxSense UA: %.2f dB\n", RxSenseUE)
	fmt.Printf("TxPowerNodeBase: %.2f dB\n", TxPowerNodeBase)
	fmt.Printf("TxPowerUserAgent: %.2f dB\n", TxPowerUserAgent)
	fmt.Printf("Radius comm : %.2f m\n", Radius)
	fmt.Printf("Square comm : %.2f m2\n", SqNodeBase)
	fmt.Printf("Speed Required : %.2f \n", SpeedRequired)
}

func binSearchDistanceByPL(min float64, max float64, find float64,
	c CourseConfig.Config) float64 {
	var (
		currentMax float64 = max
		currentMin float64 = min
		eps        float64 = 1E-6
		res        float64 = (currentMax-currentMin)/2 + currentMin
	)
	for {
		PL := getPathLoses(c, res)
		if math.Abs(PL-find) < eps || currentMax == currentMin {
			break
		}
		if PL < find {
			currentMin = res
		} else {
			currentMax = res
		}
		res = (currentMax-currentMin)/2 + currentMin
	}
	return res
}

func getRxSense(c CourseConfig.Config) (float64, float64) {
	var (
		SINRBS float64 = 0.0
		SINRUA float64 = 0.0
		resBS  float64 = 0.0
		resUA  float64 = 0.0
	)
	SINRBS, SINRUA = getRequireSINR(c)
	resBS = c.NoiseNodeBase + SINRBS + getThermalNoise(c)
	resUA = c.NoiseUserAgent + SINRUA + getThermalNoise(c)
	return resBS, resUA
}

func getRequireSINR(c CourseConfig.Config) (float64, float64) {
	var (
		resBS           float64     = 0.0
		resUA           float64     = 0.0
		spectrEffective float64     = 0.0
		min             float64     = math.MaxFloat64
		minIndex        int         = 0
		resMap          [][]float64 = [][]float64{
			{0.0625, 2.1, 0.0},
			{0.133, 2.9, 0.0},
			{0.286, 5.1, 0.0},
			{0.67, 6.3, 0.0},
			{1.33, 7.9, 0.0},
			{1.71, 9.5, 0.0},
			{1.33, 12.9, 0.0},
			{2.66, 15.4, 0.0},
			{3.6, 19.8, 0.0},
			{0.75, 16, 0.0},
			{2.25, 19.1, 0.0},
			{3, 20.2, 0.0},
			{3.75, 21.3, 0.0},
			{4.5, 24.7, 0.0},
			{5.4, 26.9, 0.0}}
	)
	spectrEffective = (c.NeedUL) / (c.BandWidth)
	if !spectr_is_print {
		fmt.Printf("Spectr Effective: [%f]", spectrEffective)
	}
	for i := range resMap {
		resMap[i][2] = math.Abs(spectrEffective - resMap[i][0])
		if min > resMap[i][2] {
			min = resMap[i][2]
			minIndex = i
		}
	}
	resBS = resMap[minIndex][1]
	min = math.MaxFloat64
	minIndex = 0
	spectrEffective = (c.NeedDL) / (c.BandWidth)
	if !spectr_is_print {
		fmt.Printf("[%f]\n", spectrEffective)
		spectr_is_print = true
	}
	for i := range resMap {
		resMap[i][2] = math.Abs(spectrEffective - resMap[i][0])
		if min > resMap[i][2] {
			min = resMap[i][2]
			minIndex = i
		}
	}
	resUA = resMap[minIndex][1]
	return resBS, resUA
}

func getThermalNoise(c CourseConfig.Config) float64 {
	var res float64 = -174 + 10*math.Log10(c.BandWidth)
	return res
}

func getPathLoses(c CourseConfig.Config, distance float64) float64 {
	var R float64 = 1
	switch c.SectorsCount {
	default:
	case 1:
		R = math.Sqrt(c.Square / 2.6)
	case 2:
		R = math.Sqrt(c.Square / 1.73)
	case 3:
		R = math.Sqrt(c.Square / 1.95)
	}
	if !radius_is_print {
		fmt.Printf("Radius: %f m\n", R)
	}
	if c.Model == "COST" {
		if !radius_is_print {
			fmt.Printf("Use model COST321\n")
			radius_is_print = true
		}
		return cost321(c, distance)
	} else if c.Model == "FSPM" {
		if !radius_is_print {
			fmt.Printf("Use model FSPM\n")
			radius_is_print = true
		}
		return fspm(c, distance)
	}

	if (150*1E+6 <= c.FrequencyRange && c.FrequencyRange <= 2*1E+9) &&
		(30 <= c.HeightNodeBase && c.HeightNodeBase <= 200) &&
		(1 <= c.HeightUserAgent && c.HeightUserAgent <= 10) &&
		(1E+3 <= R && R <= 20E+3) {
		if !radius_is_print {
			fmt.Printf("Use model COST321\n")
			radius_is_print = true
		}
		return cost321(c, distance)
	}
	if !radius_is_print {
		fmt.Printf("Use model FSPM\n")
		radius_is_print = true
	}
	return fspm(c, distance)
}

func cost321(c CourseConfig.Config, distance float64) float64 {
	var (
		res      float64 = 0.0
		A        float64 = 0.0
		B        float64 = 0.0
		a        float64 = 0.0
		s        float64 = 0.0
		Lclutter float64 = 0.0
	)

	if 150*1E+6 <= c.FrequencyRange && c.FrequencyRange <= 1500*1E+6 {
		A = 69.55
		B = 26.16
	} else {
		A = 46.3
		B = 33.9
	}

	if (c.AreaType == "DU") || (c.AreaType == "U") {
		if c.AreaType == "DU" {
			Lclutter = 3
		} else {
			Lclutter = 0
		}
		a = 3.2*math.Pow(math.Log10(11.75*c.HeightUserAgent), 2) - 4.97
	} else if (c.AreaType == "SU") || (c.AreaType == "RU") ||
		(c.AreaType == "ROAD") {
		if c.AreaType == "SU" {
			Lclutter = -2*math.Pow(math.Log10(c.FrequencyRange*1E-6/28), 2) - 5.4
		} else if c.AreaType == "RU" {
			Lclutter = -4.78*math.Pow(math.Log10(c.FrequencyRange*1E-6), 2) +
				18.33*math.Log10(c.FrequencyRange*1E-6) - 40.94
		} else {
			Lclutter = -4.78*math.Pow(math.Log10(c.FrequencyRange*1E-6), 2) +
				18.33*math.Log10(c.FrequencyRange*1E-6) - 35.94
		}
		a = 1.1*math.Log10(c.FrequencyRange*1E-6)*c.HeightUserAgent -
			1.56*math.Log10(c.FrequencyRange*1E-6) + 0.8
	}
	if distance >= 1E+3 {
		s = 44.9 - 6.55*math.Log10(c.FrequencyRange*1E-6)
	} else {
		s = (47.88 + 13.9*math.Log10(c.FrequencyRange*1E-6) -
			13.9*math.Log10(c.HeightNodeBase)) / math.Log10(50)
	}

	res = A + B*math.Log10(c.FrequencyRange*1E-6*1E-6) -
		13.82*math.Log10(c.HeightNodeBase) - a +
		s*math.Log10(distance*1E-3) + Lclutter
	return res
}

func fspm(c CourseConfig.Config, distance float64) float64 {
	var res float64 = 20*math.Log10(distance) +
		20*math.Log10(c.FrequencyRange*1E-6) -
		27.55
	return res
}

func clrscr() {
	if runtime.GOOS == "linux" {
		cmd := exec.Command("clear")
		cmd.Stdout = os.Stdout
		cmd.Run()
	} else if runtime.GOOS == "windows" {
		cmd := exec.Command("cmd", "/c", "cls")
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
}
