.PHONY: data

regression:
	python -B src/regression.py

plot:
	python -B src/reg_plot.py

results:
	python -B src/results.py

data:
	mkdir -p data 

	cd data; curl -LO 
	cd data; curl -LO
	cd data; curl -LO

mapping:
	python -B src/mapping.py