.PHONY: data

# generating the data from the publicly available csv folder. Links for where files were downloaded located in data folder: sources.md
data:
	python -B src/group3pipe.py

# generates old data:
# need to get shape files from here first, https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_county_500k.zip
# they are not included in our uploaded data as we did not need them for our modeling.

old_data: mapping merge

select:
	python -B src/feature_selection.py

model:
	python -B src/feature_selection.py
	python -B src/regression.py

m55:
	python -B src/feature_selection55.py
	python -B src/results.py

scatter:
	python -B src/scatterG3.py

box:
	python -B src/boxplotsG3.py

heatmap:
	python -B src/heatmapG3.py

hist:
	python -B src/histogramG3.py

plots: scatter hist box heatmap 

test:
	python -B src/results_test.py

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

# Group 3 - T
