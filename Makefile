.PHONY: data

all: data mapping

model:
	python -B src/regression.py

plot:
	python -B src/reg_plot.py

results:
	python -B src/results.py

data:
	mkdir -p data 
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/jurisdictions.csv?token=GHSAT0AAAAAACDRJ3D62TJJFRFK7LZCPX7OZGJJZFA
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/stateFIPS.csv?token=GHSAT0AAAAAACDRJ3D6CVE3JBCKYOXWCFCKZGJJZYA

	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county.csv?token=GHSAT0AAAAAACDRJ3D6Q2TX37VXXUGJETKUZGJJ6AA
# geopandas files:
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.cpg
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.dbf
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.prj
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp.ea.iso.xml
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shp.iso.xml
	cd data; curl -LO https://github.com/ds5110/project-summer-2023-moriarity-tim/raw/main/data/cb_2018_us_county_500k.shx



# aidsvu files:
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/AIDSVu_County_SDOH_2020.csv?token=GHSAT0AAAAAACDRJ3D7HMIPLSQPTNGRYE6GZGJJ2PA
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county.csv?token=GHSAT0AAAAAACDRJ3D6Q2TX37VXXUGJETKUZGJJ6AA
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county45_54.csv?token=GHSAT0AAAAAACDRJ3D73JJZM6G7E4DQYUNWZGJJ5KAhttps://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county45_54.csv?token=GHSAT0AAAAAACDRJ3D73JJZM6G7E4DQYUNWZGJJ5KA
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county55%2B.csv?token=GHSAT0AAAAAACDRJ3D7SJF4EEEQDYNP75KGZGJJ6XA

mapping:
	python -B src/mapping.py