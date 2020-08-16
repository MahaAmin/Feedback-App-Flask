# Create virtual environment
setup: 
	python3 -m venv ~/.feedback-app-flask &&\
		export FLASK_APP=app.py


# Install requirements packages
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt