.PHONY: data

data: mapping merge

model:
	python -B src/regression.py

plot:
	python -B src/grp1plots.py
	python -B src/grp2plots.py

results:
	python -B src/results.py

get_data:
	mkdir -p data 
# jurisdiction table & fips codes table - generated based on links
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/jurisdictions.csv
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/stateFIPS.csv
# nursing home files
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/NH_ProviderInfo_May2023.csv
# geopandas files:
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.cpg
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.dbf
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.prj
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp.ea.iso.xml
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp.iso.xml
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shx

# aidsvu files:
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/AIDSVu_County_SDOH_2020.csv
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county.csv
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county45_54.csv
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county55%2B.csv

mapping:
	python -B src/mapping.py

merge:
	python -B src/merge.py

clean:
	rm -r data/

# Group 3