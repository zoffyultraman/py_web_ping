from flask import Flask
from flask import request
from flask import render_template
from ping_test import conn1

app = Flask(__name__)

ip = '0.0.0.0'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    global ip
    ip = request.form.get = ('ip1')
    d = conn1()
    return render_template('index.html', t=d)


if __name__ == '__main__':
    app.run()
