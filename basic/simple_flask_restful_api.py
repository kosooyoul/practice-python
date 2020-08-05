from flask import Flask, request, render_template, redirect
import datetime

app = Flask('My Simple Flask Restful API', template_folder = 'template')

@app.route('/')
def index():
    return render_template('index.html', date=datetime.datetime.now())

@app.route('/get', methods=['GET'])
def get():
    # Request parameter
    name = request.args.get('name', 'year')

    # Get datetime now
    now = datetime.datetime.now()
    nowdict = {'year': now.year, 'month': now.month, 'day': now.day, 'hour': now.hour, 'minute': now.minute, 'second': now.second}

    return {'success': True, name: nowdict.get(name)}

@app.route('/post', methods=['GET', 'POST'])
def post():
    # Check method
    if request.method != 'POST': return redirect('/')

    # Request form data
    echo = request.form.get('echo')

    return {'success': True, 'echo': echo, 'method': request.method}

if __name__ == '__main__': app.run(port = 80)

# Test Post API by Javascript on Frontend
# var xhr = new XMLHttpRequest();
# xhr.open('post', '/post', false);
# var fd = new FormData();
# fd.set('echo', 'hello anne');
# xhr.send(fd);
# console.log(xhr.response);
