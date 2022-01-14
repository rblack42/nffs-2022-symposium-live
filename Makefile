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

.PHONY: book
book:
	cd book && \
		jb build ./ --verbose
	cp -r book/_build/html/* docs

.PHONY: clean
clean:
	python scripts/clean.py
