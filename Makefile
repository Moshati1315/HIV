.PHONY: data

data:
	mkdir -p data 
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/hiv_rates45%2B.csv?token=GHSAT0AAAAAACDRJ3D7U6NEPHTRYYCD3BUSZFX6GUA
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/join_ages.csv?token=GHSAT0AAAAAACDRJ3D66DQRTECRLDSO3CVSZFX6HQA