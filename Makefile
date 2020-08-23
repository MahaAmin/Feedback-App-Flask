# Create virtual environment
setup: 
	python3 -m venv ~/.feedback-app-flask &&\
		export FLASK_APP=app.py &&\
		export FLASK_ENV=development


# Install requirements packages
install:
	pip install --upgrade pip &&\
		pip install -r requirments.txt