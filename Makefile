.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: reqs
reqs:
	pip install -U pip
	pip install -r requirements.txt

.PHONY: nb
nb:
	cd book && \
		jupyter notebook

.PHONY: build
build:
	jb build book --all
	cp -r book/_build/html/* docs

.PHONY: clean
clean:
	python book/scripts/clean.py
