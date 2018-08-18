from flask import Flask, request

from .services import cuda_is_available

app = Flask(__name__)


@app.route('/')
def hello_api():
    return 'Hello World!\n'


@app.route('/hello_i_am')
def hello_i_am():
    '''/hello_i_am/?name=alice
    '''
    name = request.args.get('name', False)
    if name:
        return 'Hello {}!\n'.format(name)
    return 'Hello, whats your name?\n'


@app.route('/hello_i_am/<string:name>')
def hello_i_am_api(name):
    '''/hello_i_am/alice
    '''
    return 'Hello {}!\n'.format(name)


@app.route('/cuda_is_available')
def cuda_is_available_api():
    return cuda_is_available()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
