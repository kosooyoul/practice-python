from flask import Flask
app = Flask('My Simple Flask Web')

@app.route('/')
def hello():
	return '<h1>Hello World!</h1><br><a href="/test">Goto Test Page</a>'

@app.route('/test')
def test():
	return '<h1>Test Page</h1>'

# Run by Flask on terminal
# export FLASK_APP=simple_flask_web.py
# flask run
# or
# set FLASK_APP=simple_flask_web.py
# flask run

# Use another port
# flask run --port 5100