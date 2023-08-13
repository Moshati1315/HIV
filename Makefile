.PHONY: data

# Generates the data from the publicly available csv folder. Links for where files were downloaded located in data folder: sources.md
# --- Group 3 data pipeline doesn't need the shape files that Group 2 needs, so we adjusted the pipeline.
data:
	python -B src/group3pipe.py

# generates the dataframe created at the end of Group2s work: Might be useful to another group if all groups results are ever pulled together.
old_data: mapping merge

#Performs Forward & Backward Feature Selection & Runs Model using the Full Population
model:
	python -B src/feature_selection.py
	python -B src/regression.py

#Performs Forward & Backward Feature Selection & Runs Model using the 55+ Population
m55:
	python -B src/feature_selection55.py
	python -B src/results.py

#Creates Histogram of Features
hist:
	python -B src/histogramG3.py

#Creates Scatterplots of Features vs. HIV Rates for the Full Population
scatter:
	python -B src/scatterG3.py

#Creates Boxplots of Features for the Full Population
box:
	python -B src/boxplotsG3.py

#Creates Heatmap of Features for the Full Population
heatmap:
	python -B src/heatmapG3.py

#Runs all the plots for the Full Population
plots: scatter hist box heatmap 

#Creates Scatterplots of Features vs. HIV Rates for the 55+ Population
scatter55:
	python -B src/55scatterG3.py

#Runs all the plots for the 55+ Population
plot55: scatter55
 
#Group 1 Data for Old Merge
mapping:
	python -B src/mapping.py
	python -B src/gdf2.py

#Group2 Data for Old Merge
merge:
	python -B src/merge.py

#Removes created data
clean:
	rm data/group3data.csv
	rm data/v1stateFIPS_df.csv

#Removes created old data
clean_old:
	rm data/gdf2.csv 
	rm data/join_ages.csv 
	rm data/v1stateFIPS_df.csv


# Group 3 - TM
