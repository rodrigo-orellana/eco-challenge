install:
	pip install -r requirements.txt
	
test:
	#python3 -m unittest discover tests
	python3 -m unittest tests/test_desafio.py

