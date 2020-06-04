package CourseConfig

import (
	"encoding/json"
	"fmt"
	"os"
)

type Config struct {
	Variant             int64   `json:"Variant"`
	FrequencyRange      float64 `json:"FrequencyRange"`
	DuplexMode          string  `json:"DuplexMode"`
	BandWidth           float64 `json:"BandWidth"`
	TxPowerNodeBase     float64 `json:"TxPowerNodeBase"`
	AntennaGainNodeBase float64 `json:"AntennaGainNodeBase"`
	FeederLoses         float64 `json:"FeederLoses"`
	AreaType            string  `json:"AreaType"`
	NeedUL              float64 `json:"NeedUL"`
	NeedDL              float64 `json:"NeedDL"`
	NoiseNodeBase       float64 `json:"NoiseNodeBase"`
	NoiseUserAgent      float64 `json:"NoiseUserAgent"`
	HeightNodeBase      float64 `json:"HeightNodeBase"`
	HeightUserAgent     float64 `json:"HeightUserAgent"`
	PenetrationLoss     float64 `json:"PenetrationLoss"`
	Square              float64 `json:"Square"`
	AbonentsCount       float64   `json:"AbonentsCount"`
	MaxDL               float64 `json:"MaxDL"`
	SectorsCount        int64   `json:"SectorsCount"`
	ENodeBCountForSGW   int64   `json:"ENodeBCountForSGW"`
	ENodeBCountForMME   int64   `json:"ENodeBCountForMME"`
	RBCount               float64 `json:"RBCount"`
	Model               string  `json:"Model"`
}

var (
	Test Config = Config{
		1,
		2.6 * 1E+9,
		"FDD",
		5 * 1E+6,
		10,
		21,
		2,
		"DU",
		1 * 1E+6,
		2 * 1E+6,
		2,
		7,
		50,
		1.5,
		28,
		200 * 1E+9,
		240 * 1E+3,
		10 * 1E+6,
		1,
		100,
		250,
		25,
		""}
	Alex Config = Config{
		8,
		3.4 * 1E+9,
		"FDD",
		15 * 1E+6,
		5,
		17,
		0.6,
		"FS",
		1.256 * 1E+6,
		2.5 * 1E+6,
		3,
		6.5,
		35,
		1.5,
		26,
		19 * 1E+9,
		75 * 1E+3,
		10 * 1E+6,
		1,
		190,
		390,
		75,
		""}
	Ilya Config = Config{
		0,
		0.84 * 1E+9,
		"FDD",
		20 * 1E+6,
		40,
		15,
		3,
		"SU",
		0.256 * 1E+6,
		0.9 * 1E+6,
		2,
		7,
		80,
		1.7,
		12,
		320 * 1E+9,
		250 * 1E+3,
		13 * 1E+6,
		2,
		170,
		290,
		100,
		""}
	Sergey Config = Config{
		5,
		3.6 * 1E+9,
		"FDD",
		5 * 1E+6,
		4,
		19,
		0.4,
		"FS",
		0.512 * 1E+6,
		1.1 * 1E+6,
		2.4,
		6.5,
		20,
		1.6,
		19,
		10 * 1E+9,
		100 * 1E+3,
		13 * 1E+6,
		1,
		140,
		270,
		25,
		""}
	Elena Config = Config{
		6,
		1.95 * 1E+9,
		"FDD",
		10 * 1E+6,
		40,
		19,
		1,
		"DU",
		0.256 * 1E+6,
		1.2 * 1E+6,
		2.5,
		7.4,
		40,
		1.7,
		25,
		180 * 1E+9,
		260 * 1E+3,
		10 * 1E+6,
		3,
		160,
		450,
		50,
		""}
)

func getJsonConfig(c Config) []byte {
	config_json, _ := json.Marshal(c)
	return config_json
}

func PrintJsonConfig(c Config) {
	config_json := getJsonConfig(c)
	fmt.Fprintln(os.Stderr, string(config_json))
}
