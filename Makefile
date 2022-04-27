.PHONY: env
env:
	mamba env create -f environment.yml
	conda activate ligo
	python -m ipykernel install --user --name ligo --display-name "LIGO"

html:
	jupyter-book build .

html-hub: 
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	
.PHONY: clean
clean:
	rm -rf figures/*.png
	rm -rf audio/*.wav
	rm -rf _build/*