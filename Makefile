.PHONY: data

# generating the data from the publicly available csv folder. Links for where files were downloaded located in sourcesmake re.md
data: mapping merge

model:
	python -B src/regression.py

m55:
	python -B src/results.py

mapping:
	python -B src/mapping.py
	python -B src/gdf2.py

merge:
	python -B src/merge.py

# to clean created data
clean:
	rm data/gdf2.csv 
	rm data/join_ages.csv 
	rm data/v1stateFIPS_df.csv

# Group 3