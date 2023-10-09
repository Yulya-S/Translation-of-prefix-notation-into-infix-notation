all:
	coverage run -m pytest tests
	coverage html

run: all
	python app/main.py
