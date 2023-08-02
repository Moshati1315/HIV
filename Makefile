.PHONY: data

data: mapping merge

model:
	python -B src/regression.py

plot:
	python -B src/grp1plots.py
	python -B src/grp2plots.py

results:
	python -B src/results.py

# to download from repo directly, not necessary if cloning the repo all the starting files are in the data folder.
get_data:
	mkdir -p data 
# jurisdiction table & fips codes table - generated based on links
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/jurisdictions.csv?token=GHSAT0AAAAAACDRJ3D6GJL2SOHUKY4O7CKWZGJYQXQ
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/stateFIPS.csv?token=GHSAT0AAAAAACDRJ3D6VIECQQEZ4W2C4F6KZGJYNUA
# nursing home files
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/NH_ProviderInfo_May2023.csv?token=GHSAT0AAAAAACDRJ3D63FLRQ2ZPONEODZWKZGJYMKA
# geopandas files:
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.cpg
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.dbf
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.prj
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp.ea.iso.xml
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp.iso.xml
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shx

# aidsvu files:
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/AIDSVu_County_SDOH_2020.csv?token=GHSAT0AAAAAACDRJ3D75RPF653ZUKRPCM54ZGJYK7Q
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county.csv?token=GHSAT0AAAAAACDRJ3D7JEEZGFS27W7WDVRYZGJYONQ
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county45_54.csv?token=GHSAT0AAAAAACDRJ3D7BH6HCT53E7IWIJN6ZGJYO2A
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county55%2B.csv?token=GHSAT0AAAAAACDRJ3D7VCYIBD7O6QYPLUZSZGJYPGA

mapping:
	python -B src/mapping.py

merge:
	python -B src/gdf2.py
	python -B src/merge.py

clean:
	rm -r data/

# Group 3


