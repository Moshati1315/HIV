.PHONY: data

regression:
	python -B src/regression.py

plot:
	python -B src/reg_plot.py

results:
	python -B src/results.py

data:
	mkdir -p data 
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/AIDSVu_County_SDOH_2020.csv?token=GHSAT0AAAAAACDRJ3D6U2GDBG4Z4P2TIEPAZGCOK3Q
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county.csv?token=GHSAT0AAAAAACDRJ3D6SWLUIUOPZXMT2O22ZGCOL6Q
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county45_54.csv?token=GHSAT0AAAAAACDRJ3D65EYFHIBGGBBLOQ3OZGCOMXQ
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county55%2B.csv?token=GHSAT0AAAAAACDRJ3D6RBPIN2RTXJI5D3E2ZGCONHQ